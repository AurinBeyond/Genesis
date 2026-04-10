"""
GENESIS Queue Engine v1.0
Agent: 0.3 System Orchestrator

Scans runtime/QUEUE.md, processes READY tasks whose dependencies are met,
updates task states, generates runtime/SUMMARY.md, and appends to logs.

Log format (LOGGING-STANDARDS.md v1.1):
  [YYYY-MM-DDTHH:MM:SSZ] | SOURCE | ACTION | TARGET | STATUS | DETAIL

Run via:
  python scripts/queue_engine.py

Or triggered by .github/workflows/genesis-queue-runner.yml (scheduled).
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
QUEUE_FILE = REPO_ROOT / "runtime" / "QUEUE.md"
STATE_FILE = REPO_ROOT / "runtime" / "STATE.json"
AGENT_STATUS_FILE = REPO_ROOT / "runtime" / "AGENT-STATUS.json"
SCHEDULE_FILE = REPO_ROOT / "runtime" / "SCHEDULE.json"
SUMMARY_FILE = REPO_ROOT / "runtime" / "SUMMARY.md"

LOG_UPDATES = REPO_ROOT / "logs" / "updates.log"
LOG_FAILURES = REPO_ROOT / "logs" / "failures.log"
LOG_DECISIONS = REPO_ROOT / "logs" / "decisions.log"

AGENT_ID = "0.3 System Orchestrator"

# ── Task state constants ─────────────────────────────────────────────────────

STATE_NEW = "NEW"
STATE_READY = "READY"
STATE_RUNNING = "RUNNING"
STATE_REVIEW = "REVIEW"
STATE_DONE = "DONE"
STATE_BLOCKED = "BLOCKED"

# ── Logging ──────────────────────────────────────────────────────────────────

def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _append(log_path: Path, line: str) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def log_update(action: str, target: str, status: str, detail: str = "") -> None:
    line = f"{_ts()} | {AGENT_ID} | {action} | {target} | {status} | {detail}"
    _append(LOG_UPDATES, line)
    print(line)


def log_failure(action: str, target: str, detail: str) -> None:
    line = f"{_ts()} | {AGENT_ID} | {action} | {target} | FAILED | {detail}"
    _append(LOG_FAILURES, line)
    print(f"[FAILURE] {line}", file=sys.stderr)


def log_decision(action: str, target: str, detail: str) -> None:
    line = f"{_ts()} | {AGENT_ID} | {action} | {target} | REVIEW_REQUIRED | {detail}"
    _append(LOG_DECISIONS, line)
    print(f"[DECISION] {line}")


# ── Schedule gate ─────────────────────────────────────────────────────────────

def _parse_hour_range(hhmm_range: str) -> tuple[int, int]:
    """Parse 'HH:MM-HH:MM' into (start_minutes, end_minutes)."""
    start, end = hhmm_range.split("-")
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return sh * 60 + sm, eh * 60 + em


def load_schedule() -> dict:
    if not SCHEDULE_FILE.exists():
        log_failure("LOAD", str(SCHEDULE_FILE), "SCHEDULE.json missing; using defaults")
        return {
            "autonomous_hours": "00:00-17:00",
            "review_window": "18:00-22:00",
            "restricted_actions": ["publish", "payment", "external_api_write"],
        }
    return json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))


def current_mode(schedule: dict) -> str:
    """Return 'AUTONOMOUS', 'REVIEW', or 'RESTRICTED'."""
    now = datetime.now(timezone.utc)
    now_min = now.hour * 60 + now.minute
    auto_start, auto_end = _parse_hour_range(schedule["autonomous_hours"])
    rev_start, rev_end = _parse_hour_range(schedule["review_window"])
    if auto_start <= now_min < auto_end:
        return "AUTONOMOUS"
    if rev_start <= now_min < rev_end:
        return "REVIEW"
    return "RESTRICTED"


def action_allowed(action: str, schedule: dict, mode: str) -> bool:
    if mode == "RESTRICTED":
        return False
    if action in schedule.get("restricted_actions", []):
        return False
    return True


# ── Queue parsing ─────────────────────────────────────────────────────────────

_TABLE_ROW = re.compile(r"^\s*\|(.+)\|\s*$")
_SEPARATOR = re.compile(r"^\s*\|[-| :]+\|\s*$")

TASK_FIELDS = [
    "id", "title", "agent_owner", "priority", "state",
    "created_at", "updated_at", "dependencies", "output_path",
]


def _parse_table_row(line: str) -> list[str] | None:
    m = _TABLE_ROW.match(line)
    if not m:
        return None
    return [cell.strip() for cell in m.group(1).split("|")]


def load_queue() -> tuple[list[dict], list[str]]:
    """Return (tasks, raw_lines). Logs failure if file missing."""
    if not QUEUE_FILE.exists():
        log_failure("LOAD", str(QUEUE_FILE), "QUEUE.md missing")
        return [], []

    raw_lines = QUEUE_FILE.read_text(encoding="utf-8").splitlines()
    tasks: list[dict] = []
    header_found = False
    separator_found = False

    for line in raw_lines:
        if _SEPARATOR.match(line):
            separator_found = True
            continue
        cells = _parse_table_row(line)
        if cells is None:
            continue
        if not header_found:
            if cells[0].strip().lower() == "id":
                header_found = True
            continue
        if not separator_found:
            continue
        if len(cells) < len(TASK_FIELDS):
            continue
        task = dict(zip(TASK_FIELDS, cells[: len(TASK_FIELDS)]))
        tasks.append(task)

    return tasks, raw_lines


def save_queue(tasks: list[dict], raw_lines: list[str]) -> None:
    """Write back updated task rows into QUEUE.md, preserving all other content."""
    task_index = {t["id"]: t for t in tasks}
    new_lines: list[str] = []
    in_table = False
    separator_found = False

    for line in raw_lines:
        if _SEPARATOR.match(line):
            separator_found = True
            in_table = True
            new_lines.append(line)
            continue
        cells = _parse_table_row(line)
        if cells and in_table and separator_found:
            row_id = cells[0].strip()
            if row_id in task_index:
                t = task_index[row_id]
                padded = [t.get(f, "") for f in TASK_FIELDS]
                new_lines.append("| " + " | ".join(padded) + " |")
                continue
        new_lines.append(line)

    QUEUE_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


# ── Dependency check ──────────────────────────────────────────────────────────

def dependencies_satisfied(task: dict, all_tasks: list[dict]) -> bool:
    deps_raw = task.get("dependencies", "none").strip().lower()
    if deps_raw in ("", "none", "-"):
        return True
    dep_ids = [d.strip() for d in deps_raw.split(",") if d.strip()]
    done_ids = {t["id"] for t in all_tasks if t["state"] == STATE_DONE}
    unsatisfied = [d for d in dep_ids if d not in done_ids]
    if unsatisfied:
        log_update(
            "DEPENDENCY_CHECK", task["id"], "PENDING",
            f"Waiting on: {', '.join(unsatisfied)}"
        )
        return False
    return True


# ── Task execution ────────────────────────────────────────────────────────────

# Map of task IDs or title keywords to the script that executes them.
# Add entries here as new executable tasks are introduced.
_TASK_DISPATCH: dict[str, str] = {
    "matrix_bridge": "scripts/matrix_bridge.py",
    "stripe": "scripts/matrix_bridge.py",
}


def _dispatch_script(task: dict) -> str | None:
    """Return script path for task, or None if no executable handler."""
    title_lower = task["title"].lower()
    for keyword, script in _TASK_DISPATCH.items():
        if keyword in title_lower or keyword in task["id"].lower():
            return script
    return None


def execute_task(task: dict, schedule: dict, mode: str) -> str:
    """
    Execute a single task. Returns final state: DONE, REVIEW, or BLOCKED.
    Writes output to task['output_path'] when applicable.
    """
    tid = task["id"]
    script = _dispatch_script(task)

    if script:
        script_path = REPO_ROOT / script
        if not script_path.exists():
            log_failure("EXECUTE", tid, f"Script not found: {script}")
            return STATE_BLOCKED

        # Check restricted actions
        for restricted in schedule.get("restricted_actions", []):
            if restricted in task["title"].lower() or restricted in script:
                if not action_allowed(restricted, schedule, mode):
                    log_update("SKIP", tid, "BLOCKED",
                               f"Action '{restricted}' restricted in mode {mode}")
                    log_decision("DEFER", tid,
                                 f"Task deferred — restricted action '{restricted}' during {mode}")
                    return STATE_BLOCKED

        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True, text=True, timeout=120,
                cwd=str(REPO_ROOT),
            )
            output = result.stdout.strip()
            if result.returncode != 0:
                log_failure("EXECUTE", tid, result.stderr.strip() or "Non-zero exit")
                return STATE_BLOCKED

            # Write output if output_path is specified
            out_path_str = task.get("output_path", "").strip()
            if out_path_str and out_path_str not in ("", "-", "none"):
                out_path = REPO_ROOT / out_path_str
                out_path.parent.mkdir(parents=True, exist_ok=True)
                if output:
                    out_path.write_text(output, encoding="utf-8")

            log_update("EXECUTE", tid, "SUCCESS", output[:120] if output else "completed")
            return STATE_DONE

        except subprocess.TimeoutExpired:
            log_failure("EXECUTE", tid, "Timeout after 120s")
            return STATE_BLOCKED
        except Exception as exc:
            log_failure("EXECUTE", tid, str(exc))
            return STATE_BLOCKED

    # No script handler — built-in tasks
    title_lower = task["title"].lower()

    if "summary" in title_lower:
        # Self-referential: generating SUMMARY.md is handled at end of run
        log_update("EXECUTE", tid, "SUCCESS", "SUMMARY.md will be written by engine")
        return STATE_DONE

    # Unknown task with no handler — requires human review
    log_update("EXECUTE", tid, "REVIEW_REQUIRED",
               "No automated handler; flagged for human review")
    log_decision("REVIEW", tid, "No handler registered for this task")
    return STATE_REVIEW


# ── State management ──────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log_failure("LOAD", str(STATE_FILE), "STATE.json corrupt; resetting")
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def update_agent_status(agent: str, task_id: str | None, status: str) -> None:
    data: dict = {}
    if AGENT_STATUS_FILE.exists():
        try:
            data = json.loads(AGENT_STATUS_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    agents = data.setdefault("agents", {})
    agents[agent] = {
        "last_task": task_id,
        "status": status,
        "updated_at": _ts(),
    }
    AGENT_STATUS_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


# ── Summary generation ────────────────────────────────────────────────────────

def generate_summary(tasks: list[dict], mode: str, health: str) -> None:
    done = [t for t in tasks if t["state"] == STATE_DONE]
    running = [t for t in tasks if t["state"] == STATE_RUNNING]
    blocked = [t for t in tasks if t["state"] == STATE_BLOCKED]
    review = [t for t in tasks if t["state"] == STATE_REVIEW]
    new_ready = [t for t in tasks if t["state"] in (STATE_NEW, STATE_READY)]

    def task_row(t: dict) -> str:
        return f"- **{t['id']}** — {t['title']} _(owner: {t['agent_owner']}, priority: {t['priority']})_"

    lines = [
        "# GENESIS DAILY SUMMARY",
        f"_Generated: {_ts()} UTC | Mode: {mode} | Health: {health}_",
        "",
        "## ✅ Completed Tasks",
    ]
    lines += [task_row(t) for t in done] if done else ["_(none)_"]
    lines += [
        "",
        "## 🔄 In Progress",
    ]
    lines += [task_row(t) for t in running] if running else ["_(none)_"]
    lines += [
        "",
        "## ⏳ Pending (NEW / READY)",
    ]
    lines += [task_row(t) for t in new_ready] if new_ready else ["_(none)_"]
    lines += [
        "",
        "## 👤 Required Human Decisions (REVIEW)",
    ]
    if review:
        for t in review:
            lines.append(task_row(t))
    else:
        lines.append("_(none)_")

    lines += [
        "",
        "## 🔴 BLOCKED",
    ]
    if blocked:
        for t in blocked:
            lines.append(task_row(t))
    else:
        lines.append("_(none)_")

    lines += [
        "",
        "## CRITICAL",
        "_(see logs/failures.log for details)_" if blocked else "_(no critical issues)_",
        "",
        "## ⚙️ System Health",
        f"- Status: **{health}**",
        f"- Mode: {mode}",
        f"- Total tasks: {len(tasks)}",
        f"- Done: {len(done)} | Running: {len(running)} | Blocked: {len(blocked)} | Review: {len(review)}",
        f"- Last run: {_ts()}",
    ]

    SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log_update("GENERATE", str(SUMMARY_FILE), "SUCCESS", "SUMMARY.md updated")


# ── Duplicate detection ───────────────────────────────────────────────────────

def check_duplicates(tasks: list[dict]) -> list[dict]:
    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    dupes: list[dict] = []
    for t in tasks:
        tid = t["id"]
        title = t["title"].strip().lower()
        if tid in seen_ids or title in seen_titles:
            log_failure("DUPLICATE", tid, f"Duplicate task detected: {t['title']}")
            dupes.append(t)
        seen_ids.add(tid)
        seen_titles.add(title)
    return dupes


# ── Main loop ─────────────────────────────────────────────────────────────────

def run() -> None:
    log_update("START", "queue_engine", "PENDING", "Queue engine starting")

    # Load schedule and determine mode
    schedule = load_schedule()
    mode = current_mode(schedule)
    log_update("MODE", "queue_engine", "SUCCESS", f"Current mode: {mode}")

    # Load queue
    tasks, raw_lines = load_queue()
    if not tasks and not raw_lines:
        log_failure("LOAD", str(QUEUE_FILE), "Cannot proceed without QUEUE.md")
        return

    # Check for duplicates (fail fast)
    dupes = check_duplicates(tasks)
    for d in dupes:
        d["state"] = STATE_BLOCKED
        d["updated_at"] = _ts()

    # In REVIEW mode, surface REVIEW tasks to decisions.log and skip execution
    if mode == "REVIEW":
        for t in tasks:
            if t["state"] == STATE_REVIEW:
                log_decision("SURFACE", t["id"],
                             f"Review window active — awaiting human decision on: {t['title']}")
        generate_summary(tasks, mode, "REVIEW_WINDOW")
        save_queue(tasks, raw_lines)
        return

    # Select READY tasks with satisfied dependencies
    ready_tasks = [
        t for t in tasks
        if t["state"] == STATE_READY and dependencies_satisfied(t, tasks)
    ]

    if not ready_tasks:
        log_update("SCAN", "QUEUE.md", "SUCCESS", "No READY tasks with satisfied dependencies")
        generate_summary(tasks, mode, "IDLE")
        save_state({
            **load_state(),
            "last_run": _ts(),
            "mode": mode,
            "active_tasks": 0,
            "blocked_tasks": sum(1 for t in tasks if t["state"] == STATE_BLOCKED),
            "done_tasks": sum(1 for t in tasks if t["state"] == STATE_DONE),
            "review_tasks": sum(1 for t in tasks if t["state"] == STATE_REVIEW),
            "system_health": "IDLE",
        })
        save_queue(tasks, raw_lines)
        return

    # Process each ready task
    update_agent_status(AGENT_ID, None, "RUNNING")
    processed = 0
    failed = 0

    for task in ready_tasks:
        tid = task["id"]
        log_update("LOCK", tid, "RUNNING", f"Locking task: {task['title']}")

        # Mark RUNNING in memory (not persisted mid-run to avoid partial writes)
        task["state"] = STATE_RUNNING
        task["updated_at"] = _ts()

        # Execute
        final_state = execute_task(task, schedule, mode)

        task["state"] = final_state
        task["updated_at"] = _ts()

        log_update("COMPLETE", tid, final_state, f"Task '{task['title']}' → {final_state}")

        if final_state == STATE_BLOCKED:
            failed += 1
        else:
            processed += 1

    update_agent_status(AGENT_ID, ready_tasks[-1]["id"] if ready_tasks else None, "IDLE")

    # Persist queue
    save_queue(tasks, raw_lines)

    # Update state
    health = "OK" if failed == 0 else ("DEGRADED" if processed > 0 else "ERROR")
    save_state({
        **load_state(),
        "last_run": _ts(),
        "mode": mode,
        "active_tasks": 0,
        "blocked_tasks": sum(1 for t in tasks if t["state"] == STATE_BLOCKED),
        "done_tasks": sum(1 for t in tasks if t["state"] == STATE_DONE),
        "review_tasks": sum(1 for t in tasks if t["state"] == STATE_REVIEW),
        "system_health": health,
    })

    # Generate summary
    generate_summary(tasks, mode, health)

    log_update(
        "END", "queue_engine", "SUCCESS",
        f"Run complete — processed: {processed}, failed: {failed}, mode: {mode}"
    )


if __name__ == "__main__":
    run()
