# LOGGING STANDARD v1.0
# AurinBeyond / Genesis — Execution Memory Layer
# Status: ACTIVE

---

## 1. PURPOSE

This document defines the required logging system for all GENESIS runtime executions.

**Why logging is required:**
- Execution without logging is invisible. Invisible execution cannot be debugged, audited, or improved.
- Agents operate autonomously. Logging is the only persistent record of what they did and why.
- System failures must be traceable to their origin. Silent errors compound into undiagnosed drift.

**Problems it prevents:**
- Undetected failures that corrupt downstream output
- Decisions made without a traceable rationale
- Inability to reproduce or explain system behavior
- Loss of execution history after task completion

**How it enables debugging and optimization:**
- Every failure has a logged reason and state
- Every routing decision is traceable to its trigger condition
- Execution flow can be replayed from logs alone

**How it improves transparency:**
- The source can inspect any task execution end-to-end
- Agents cannot act without producing a record
- System behavior becomes auditable over time

> If it is not logged, it did not happen.

---

## 2. LOG TYPES

Three logs exist. Each has a single purpose. They do not overlap.

### `updates.log`

Tracks: completed tasks, file changes, execution flow steps, system state updates.

Used to answer: *What happened? What changed? What is the current state?*

Location: `logs/updates.log`

---

### `decisions.log`

Tracks: agent routing decisions, approve / modify / reject outcomes, strategic choices, branching logic.

Used to answer: *Why did the system go this direction? What was chosen and by whom?*

Location: `logs/decisions.log`

---

### `failures.log`

Tracks: validation failures, runtime errors, blocked executions, missing input cases, incomplete outputs.

Used to answer: *What went wrong? Where did execution stop? Can it be retried?*

Location: `logs/failures.log`

---

## 3. LOG ENTRY STRUCTURE

Every log entry must follow this exact format:

```
[YYYY-MM-DD HH:MM] TASK-ID → event: description — result: SUCCESS|WARNING|FAIL (AGENT)
```

**Fields:**

| Field | Description |
|---|---|
| `[YYYY-MM-DD HH:MM]` | Timestamp in ISO 8601 format |
| `TASK-ID` | Unique task identifier (e.g. TASK-001) or system reference |
| `event` | Category: `started`, `completed`, `decision`, `failure`, `blocked`, `validated`, `routed` |
| `description` | Short, specific explanation of what occurred |
| `result` | One of: `SUCCESS`, `WARNING`, `FAIL` |
| `(AGENT)` | The agent or system component responsible for the entry |

**Rules:**
- Each entry is one line
- No line breaks within an entry
- Append only — never edit existing entries
- Entries must be written at the moment the event occurs, not retrospectively

---

## 4. TIMESTAMP RULE

- All timestamps use ISO 8601: `YYYY-MM-DD HH:MM`
- Seconds are optional; minutes are required
- All times are recorded in UTC
- No missing timestamps — an entry without a timestamp is invalid
- Entries must appear in chronological order within each log file

---

## 5. TASK IDENTIFICATION RULE

- Every log entry references a task by its ID (e.g. `TASK-001`, `TASK-002`)
- System-level events not tied to a specific task use `SYSTEM`
- Task IDs must match the IDs defined in `TASKMASTER.md`
- The same task ID must appear consistently across all three logs
- Task ID must not be abbreviated, altered, or omitted

---

## 6. LOGGING MOMENTS

The following events require a log entry. These are not optional.

| Moment | Log File | Required |
|---|---|---|
| Input accepted | `updates.log` | Yes |
| Input rejected | `failures.log` | Yes |
| Agent routing decision | `decisions.log` | Yes |
| Execution started | `updates.log` | Yes |
| Step completed | `updates.log` | Yes |
| Output generated | `updates.log` | Yes |
| Validation passed | `updates.log` | Yes |
| Validation failed | `failures.log` | Yes |
| Execution completed | `updates.log` | Yes |
| Execution blocked | `failures.log` | Yes |
| Strategic decision made | `decisions.log` | Yes |

No execution phase may pass without a log entry at each required moment.

---

## 7. FAILURE LOGGING RULE

- Every failure must produce an entry in `failures.log`
- No silent errors — if execution fails without a log entry, the logging system has failed
- Failure entries must include:
  - The reason for failure
  - The state the task is left in (`BLOCKED`, `INVALID`, `INCOMPLETE`)
  - Whether a retry is possible (`retry: YES` or `retry: NO`)

**Failure entry format:**

```
[YYYY-MM-DD HH:MM] TASK-ID → failure: description — state: BLOCKED|INVALID|INCOMPLETE — retry: YES|NO (AGENT)
```

---

## 8. DECISION TRACEABILITY

- Every routing or strategic decision must be written to `decisions.log`
- Decision entries must include a short rationale (one clause is sufficient)
- The system must be able to answer "why did this happen" from the log alone
- Decisions that affect downstream tasks must be visible before those tasks run

**Decision entry format:**

```
[YYYY-MM-DD HH:MM] TASK-ID → decision: description — reason: short rationale (AGENT)
```

---

## 9. NON-BLOAT LOGGING RULE

- Each log entry must be one line and contain only what is necessary
- Do not duplicate the same event across multiple log files
- Do not narrate what the agent is "thinking" — only log observable actions and results
- Each log type has a distinct scope; do not write update entries into `decisions.log` or vice versa
- Verbose explanations belong in output files, not in logs

---

## 10. LOG STORAGE STRUCTURE

```
logs/
  updates.log       — execution events and state changes
  decisions.log     — routing and strategic decisions
  failures.log      — errors, blocks, and rejections
  outputs/          — task output files (not logs)
  state-tracker.md  — current system state snapshot
```

- All log files remain in `logs/`
- Log files are not mixed with output files
- Output artifacts go in `logs/outputs/TASK-ID/`
- Log files are append-only; entries are never overwritten
- No log file is deleted without an explicit system hygiene decision recorded in `updates.log`

---

## 11. CLEANUP AND ROTATION RULE

- Log files are not deleted during active system operation
- When a log file exceeds practical review size (recommended: 500 entries), an archive copy is created:
  - Archive format: `updates-YYYY-MM.log`
  - Archive location: `logs/archive/`
  - The active log file continues from the next entry after archiving
- Archive creation must be logged in `updates.log`
- Important task history is never discarded; only moved to archive

---

## 12. SECURITY AND INTEGRITY RULE

- Log entries must not be altered after writing
- Entries must not be deleted except through a documented system hygiene process
- Any modification to a log file outside of append operations is a system integrity violation
- The log files are the authoritative record of system behavior

---

## 13. HUMAN READABILITY RULE

- Every log entry must be readable by a human without parsing tools
- Abbreviations must be consistent and defined (e.g. `AGENT`, `TASK-ID`)
- Technical identifiers must map to understandable references via `TASKMASTER.md`
- Logs must not require external context to interpret basic event meaning
- Machine-readability must not come at the cost of human comprehension

---

## 14. EXAMPLES

### Valid `updates.log` Entry

```
[2026-04-07 20:12] TASK-001 → completed: STEP 2 output generated at logs/outputs/TASK-001/02-funnel.md — result: SUCCESS (FUNNEL-ARCHITECT)
```

**Why it passes:** Timestamp present. Task ID matches. Event is specific. Result is declared. Agent is identified.

---

### Valid `decisions.log` Entry

```
[2026-04-07 20:00] TASK-001 → decision: routed to FUNNEL-ARCHITECT for step 2 — reason: task type is funnel-design and STEP 1 was approved (GENESIS-ORCHESTRATOR)
```

**Why it passes:** Decision is named. Reason is traceable. Agent is identified. Task ID is consistent with other logs.

---

### Valid `failures.log` Entry

```
[2026-04-07 19:55] TASK-003 → failure: input rejected — missing Requested Output field — state: INCOMPLETE — retry: YES (GENESIS-RUNTIME)
```

**Why it passes:** Failure is specific. State is declared. Retry is indicated. Agent is identified. Entry is one line.

---

**This standard is version-locked. Changes require a version bump in the file header.**
