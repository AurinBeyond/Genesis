"""
GENESIS Orchestrator Loop v1.0
Agent: 0.3 System Orchestrator

Continuous execution loop. Calls queue_engine.run() on every tick,
sleeps between ticks, respects SCHEDULE.json time gates, and recovers
from any crash without resetting task state.

Usage:
    python scripts/orchestrator.py              # runs until killed
    python scripts/orchestrator.py --once       # single tick then exit (CI / cron)

SCHEDULE.json controls:
    autonomous_hours  — full execution, default interval (30 s)
    review_window     — summary-only pass, slower interval (60 s)
    outside both      — restricted; loop idles and logs heartbeat only
"""

import argparse
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

# ── Bootstrap path so queue_engine is importable regardless of cwd ───────────
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import queue_engine  # noqa: E402  (must come after sys.path edit)

# ── Constants ─────────────────────────────────────────────────────────────────
AGENT_ID = "0.3 System Orchestrator"
LOOP_INTERVAL_AUTONOMOUS = 30   # seconds between ticks during autonomous hours
LOOP_INTERVAL_REVIEW = 60       # seconds during review window
LOOP_INTERVAL_RESTRICTED = 120  # seconds when outside all windows (heartbeat)

LOG_UPDATES = REPO_ROOT / "logs" / "updates.log"
LOG_FAILURES = REPO_ROOT / "logs" / "failures.log"

# ── Logging helpers ───────────────────────────────────────────────────────────

def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _log(path: Path, action: str, target: str, status: str, detail: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = f"{_ts()} | {AGENT_ID} | {action} | {target} | {status} | {detail}"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(line)


def log_update(action: str, target: str, status: str, detail: str = "") -> None:
    _log(LOG_UPDATES, action, target, status, detail)


def log_failure(action: str, target: str, detail: str) -> None:
    _log(LOG_FAILURES, action, target, "FAILED", detail)


# ── Schedule helpers ──────────────────────────────────────────────────────────

def _interval_for_mode(mode: str) -> int:
    return {
        "AUTONOMOUS": LOOP_INTERVAL_AUTONOMOUS,
        "REVIEW": LOOP_INTERVAL_REVIEW,
    }.get(mode, LOOP_INTERVAL_RESTRICTED)


# ── Single tick ───────────────────────────────────────────────────────────────

def tick() -> None:
    """Run one complete queue engine pass."""
    queue_engine.run()


# ── Main loop ─────────────────────────────────────────────────────────────────

def loop(run_once: bool = False) -> None:
    log_update("START", "orchestrator", "SUCCESS",
               "Orchestrator loop starting" + (" (single tick)" if run_once else ""))

    iteration = 0

    while True:
        iteration += 1

        # Determine current operating mode
        try:
            schedule = queue_engine.load_schedule()
            mode = queue_engine.current_mode(schedule)
        except Exception as exc:
            log_failure("SCHEDULE_READ", "SCHEDULE.json", str(exc))
            mode = "AUTONOMOUS"

        interval = _interval_for_mode(mode)

        log_update("TICK", f"iteration={iteration}", "PENDING",
                   f"mode={mode} interval={interval}s")

        # Execute queue engine pass with crash protection
        try:
            tick()
            log_update("TICK", f"iteration={iteration}", "SUCCESS",
                       f"mode={mode}")
        except Exception:
            tb = traceback.format_exc().replace("\n", " | ")
            log_failure("TICK", f"iteration={iteration}", tb)
            # FAILSAFE: never reset tasks; next tick reloads queue from disk

        if run_once:
            log_update("STOP", "orchestrator", "SUCCESS",
                       "Single-tick mode; exiting after iteration 1")
            break

        # Sleep until next tick
        log_update("SLEEP", "orchestrator", "PENDING",
                   f"Sleeping {interval}s (mode={mode})")
        time.sleep(interval)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="GENESIS Orchestrator — continuous queue execution loop"
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run a single tick then exit (useful for cron / CI)",
    )
    args = parser.parse_args()

    try:
        loop(run_once=args.once)
    except KeyboardInterrupt:
        log_update("STOP", "orchestrator", "SUCCESS",
                   "Received KeyboardInterrupt; shutting down cleanly")
        sys.exit(0)


if __name__ == "__main__":
    main()
