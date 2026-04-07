# RUNTIME SPEC v1.0
# AurinBeyond / Genesis — Execution Layer
# Status: ACTIVE

---

## 1. RUNTIME PURPOSE

Architecture without execution is documentation. The runtime layer converts the GENESIS agent architecture into controlled, traceable, real-world execution.

**Why the runtime layer exists:**
- Agent definitions, orchestration protocols, and brand rules do nothing on their own.
- The runtime provides the mechanism that moves a task from input to validated output.
- Without it, agents would act independently, in undefined order, with no accountability.

**Problems it prevents:**
- Unordered or duplicate agent execution
- Silent failures with no log trail
- Output produced without valid input
- Agents acting outside their defined scope
- Inconsistent outputs reaching users

**How it connects architecture to execution:**
The runtime reads a structured task, routes it through the correct agents in sequence, enforces validation at the output stage, and writes all decisions, completions, and failures to structured logs.

**Why architecture without runtime is incomplete:**
A blueprint without a build process produces nothing. The runtime is the build process.

---

## 2. EXECUTION ENTRY MODEL

**Entry point:** `TASKMASTER.md` — the source of all active tasks.

**Trigger file:** `.github/workflows/genesis-runtime.yml`

**Minimum required input to start execution:**
- A task exists in the `ACTIVE TASKS` section of `TASKMASTER.md` with status `pending` (unchecked)
- Core files are present: `core/GENESIS-LAWS.md`, `core/STATE.md`, `core/MODE.md`, `core/INPUT.md`, `core/TASK.md`, `agents/AGENT-BASE.md`, `AGENTS-CONFIG.md`, `TASKMASTER.md`
- `logs/updates.log` exists

**If input is incomplete:**
- Execution halts at the `validate` job
- The run exits with a `has_task=false` state
- No agent executes
- No files are modified

**Supported execution modes:**
- `manual` — `workflow_dispatch` trigger via GitHub Actions UI
- `pr` mode — changes are pushed to a branch and a PR is opened for review
- `direct` mode — changes are committed directly to the target branch
- Future: scheduled execution is structurally supported via GitHub Actions `schedule` trigger but is NOT activated by default

---

## 3. TRIGGER LOGIC

**Primary trigger:** `workflow_dispatch`
- Manually initiated from the GitHub Actions UI
- Accepts the following inputs:
  - `execution_mode` — `pr` or `direct`
  - `target_branch` — branch to operate on (default: `main`)
  - `task_scope` — optional section label in TASKMASTER.md (default: `ACTIVE TASKS`)
  - `log_only` — boolean; if `true`, validates and logs without marking the task complete

**Secondary trigger (future-ready, not active):**
- `schedule` — can be added to the workflow without structural changes
- Must NOT be activated until manual execution is stable and all validation layers are confirmed

---

## 4. INPUT STANDARD ENFORCEMENT

See `core/INPUT-STANDARD.md` for the full structured input format.

**Summary:**
- Tasks enter through `TASKMASTER.md` as unchecked items (`- [ ]`)
- Each task must have: title, task type, goal, context, constraints, requested output, and execution priority
- Execution is blocked if input is missing, malformed, or empty
- Free-form execution without structured input is not permitted

---

## 5. AGENT ROUTING LOGIC

The runtime does NOT activate all agents by default.

**Routing is determined by:**
- Task type (offer creation, funnel design, copy, structure, legal, etc.)
- Required output format
- System stage (pipeline step 1–5 or standalone task)
- Communication need (Chat Agent required?)
- Language refinement need (Language Polisher required?)
- Decision need (Brand Guardian or Semantic Core required?)

**Routing map (current active pipeline):**

| Task Type | Active Agents |
|---|---|
| Offer creation | System Orchestrator → Offer Architect |
| Funnel design | Funnel Architect |
| Raw copy | Content Producer |
| Voice refinement | Humanizer |
| Brand validation + final assembly | Brand Guardian |
| Page structure | Genesis Architect |
| Authority content | Frequency Transmitter |
| Legal pages | Legal & Compliance Guard |
| Real-time user interaction | Semantic Core → Brand Intelligence → Chat Agent → Language Polisher → Navigation System |

No agent runs unless its task type matches the active task.

---

## 6. EXECUTION ORDER

All multi-agent tasks follow this sequence. No step may be skipped.

```
1. Input check          → verify TASKMASTER.md has a valid unchecked task
2. Core file check      → verify all required system files exist
3. Semantic parsing     → extract task title, type, and goal
4. Agent routing        → determine which agents are needed
5. Agent execution      → run agents in pipeline order (see Section 5)
6. Output write         → write output to logs/outputs/TASK-XXX/[step]-[type].md
7. Output validation    → verify output against OUTPUT-VALIDATION.md rules
8. Task state update    → mark task as complete in TASKMASTER.md (unless log_only)
9. Log write            → append to logs/updates.log, logs/decisions.log
10. Failure log         → if any step fails, append to logs/failures.log
```

Each step is deterministic. Order is enforced by the workflow job dependency chain.

---

## 7. OUTPUT DESTINATION RULES

| Output Type | Destination |
|---|---|
| Final task output | `logs/outputs/TASK-XXX/FINAL.md` |
| Step outputs (intermediate) | `logs/outputs/TASK-XXX/[step]-[type].md` |
| Execution decisions | `logs/decisions.log` |
| Completed actions and state changes | `logs/updates.log` |
| Failures and validation errors | `logs/failures.log` |
| User-facing content (published) | Site pages only — never from logs/ directly |

**Separation rule:** Logs are never published directly. `logs/` is the execution audit layer. Published content originates from Source-approved FINAL.md artifacts only.

---

## 8. OUTPUT VALIDATION LAYER

See `core/OUTPUT-VALIDATION.md` for the full validation ruleset.

**Validation runs before any output is treated as final.**

If validation fails:
- Output is flagged with `[VALIDATION FAILED]`
- Failure is logged in `logs/failures.log`
- Task is NOT marked complete
- System returns to `REVIEW` state for Source action

---

## 9. LOGGING SYSTEM

Three dedicated log files. Each is append-only. No entry is ever deleted or edited.

### `logs/updates.log`
Records completed actions, file changes, and workflow state transitions.

Format:
```
[YYYY-MM-DD HH:MM] TASK-ID → action: description (AGENT)
```

### `logs/decisions.log`
Records routing decisions, agent activation logic, and approve/modify/reject decisions.

Format:
```
[YYYY-MM-DD HH:MM] TASK-ID → decision: description (AGENT)
```

### `logs/failures.log`
Records execution failures, validation failures, blocked runs, and incomplete input cases.

Format:
```
[YYYY-MM-DD HH:MM] TASK-ID → failure: description — state: BLOCKED|INVALID|INCOMPLETE (AGENT)
```

All entries are timestamped in UTC. No raw or unstructured data is written to logs.

---

## 10. FAILURE HANDLING

| Failure Type | Response |
|---|---|
| Input invalid or missing | Halt at `validate` job. Log in `failures.log`. No execution. |
| Required core file missing | Halt at `validate` job. Log in `failures.log`. |
| Agent output incomplete | Flag output. Log in `failures.log`. Do not mark task complete. |
| Validation fails | Flag output. Log in `failures.log`. Return to REVIEW state. |
| Execution stops unexpectedly | GitHub Actions job failure is visible in the run log. |

**No silent failure is permitted.** Every blocked execution produces a log entry.

---

## 11. NON-BLOAT EXECUTION RULE

The runtime must not:
- Activate agents that are not required for the current task type
- Generate files that have no defined destination or purpose
- Repeat work that is already complete and Source-approved
- Create duplicate outputs for the same task step

System Hygiene applies at the execution level, not just at the architecture level.

---

## 12. HUMAN REVIEW MODE

The runtime produces one of three status flags for every completed run:

| Status | Meaning |
|---|---|
| `READY` | Output passes validation. Safe for Source review. |
| `READY WITH REVIEW` | Output passes structural validation but contains flags. Source must review before approval. |
| `BLOCKED` | Execution failed or validation failed. Source must act before the run can continue. |

These states are written to `logs/updates.log` and surfaced in the PR description when `execution_mode = pr`.

---

## 13. FILE SAFETY RULES

1. No file in `core/` may be overwritten without an explicit version bump in the file header.
2. No agent may write to root-level files (e.g., `TASKMASTER.md`) without going through the runtime task lifecycle.
3. `logs/` files are append-only. Overwriting a log file is a system integrity failure.
4. Output files in `logs/outputs/` follow the `TASK-XXX/[step]-[type].md` naming convention. No deviation.
5. All new files created by agent execution must be within `logs/outputs/TASK-XXX/` or their defined destination.

---

## 14. SUCCESS CRITERIA

The runtime is successful if and only if:

- A task entered through the defined structure in `TASKMASTER.md`
- The correct agents were selected based on task type
- Execution followed the mandatory order in Section 6
- Output was written to the correct destination
- Output was validated before being flagged as READY
- Results were logged in `updates.log` and `decisions.log`
- Any failure was logged in `failures.log`
- No duplication, overwriting, or uncontrolled output occurred

---

**Control remains with the Source. No step publishes without Source approval.**
