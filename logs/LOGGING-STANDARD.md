# LOGGING STANDARD v1.0

## CORE PRINCIPLE

> If it is not logged, it did not happen.

---

## 1. PURPOSE

Logging is not optional. It is a system requirement.

**Why logging is required:**
- GENESIS operates with multiple agents executing sequentially and in parallel. Without logs, no single point of truth exists for what happened, when, or why.
- Failures cannot be fixed if they are not visible. Silent errors compound into system drift.
- Decisions made by agents must be auditable. A system that cannot explain itself cannot be trusted or improved.

**What problems it prevents:**
- Blind re-execution of failed tasks.
- Undetected validation failures passing downstream.
- Loss of execution context between agent handoffs.
- Inability to trace the source of a degraded output.

**How it enables debugging and optimization:**
- Every task has a traceable lifecycle: input accepted → routed → executed → validated → completed or failed.
- Pattern analysis across `decisions.log` reveals routing inefficiencies.
- `failures.log` surfaces recurring failure modes that require system-level fixes, not one-off patches.

**How it improves system transparency:**
- Every agent action is visible without requiring system owner intervention.
- System behavior can be analyzed at any time without running the system again.
- Logs serve as the authoritative record of what GENESIS did and why.

---

## 2. LOG TYPES

Three logs exist. Each has a distinct purpose. They must not be mixed.

---

### `updates.log`

**Purpose:** Record of what happened during execution.

Tracks:
- Completed tasks
- File changes (created, modified, deleted)
- Execution flow steps (start, handoff, completion)
- System state updates

This log answers: *What did the system do?*

---

### `decisions.log`

**Purpose:** Record of why the system made a choice.

Tracks:
- Agent routing decisions (which agent received which task)
- Approve / modify / reject outcomes from validation
- Strategic choices made by Brand Intelligence or Orchestration
- Branching logic triggered by conditions

This log answers: *Why did the system behave this way?*

---

### `failures.log`

**Purpose:** Record of every point where the system could not proceed as expected.

Tracks:
- Validation failures (output did not meet standard)
- Runtime errors (agent unable to execute)
- Blocked executions (dependency not met)
- Missing input cases (required field absent)
- Incomplete outputs (execution stopped before completion)

This log answers: *Where did the system break, and why?*

---

## 3. LOG ENTRY STRUCTURE

Every entry across all three logs must follow this format exactly:

```
[TIMESTAMP] | TASK: <task-id-or-title> | TYPE: <UPDATE|DECISION|FAILURE> | AGENT: <agent-name> | ACTION: <what happened> | RESULT: <SUCCESS|WARNING|FAIL> | NOTE: <short explanation>
```

**Field definitions:**

| Field       | Description                                              |
|-------------|----------------------------------------------------------|
| TIMESTAMP   | ISO 8601 UTC datetime                                    |
| TASK        | Unique task ID or stable task title (must match INPUT)   |
| TYPE        | One of: UPDATE, DECISION, FAILURE                        |
| AGENT       | Name of agent that performed or triggered the action     |
| ACTION      | Short verb phrase describing what occurred               |
| RESULT      | One of: SUCCESS, WARNING, FAIL                           |
| NOTE        | One sentence explaining context, reason, or outcome      |

**Constraints:**
- All fields are mandatory. No field may be blank.
- NOTE must be a single sentence. No multi-line notes.
- Entries are written in plain text. No nested structures.
- Each entry occupies one line.

---

## 4. TIMESTAMP RULE

- All timestamps use ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`
- All timestamps are UTC. No local timezone offsets.
- No entry may be written without a timestamp.
- Entries within a log file are ordered chronologically, oldest first.
- No retroactive timestamp modification is permitted.

Example: `2026-04-07T23:41:29Z`

---

## 5. TASK IDENTIFICATION RULE

- Every task must carry a consistent identifier across all logs.
- Preferred format: `TASK-<NNN>` (e.g., `TASK-007`) assigned at input acceptance.
- If a human-readable title is used instead of an ID, it must remain identical across all log entries referencing that task.
- The identifier used in logs must match the identifier in the originating INPUT reference.
- No abbreviations, aliases, or paraphrasing of task identifiers.

---

## 6. LOGGING MOMENTS

Logs must be written at the following points. These are not optional.

| Moment                    | Log File       | Result Values            |
|---------------------------|----------------|--------------------------|
| Input accepted            | `updates.log`  | SUCCESS                  |
| Input rejected            | `failures.log` | FAIL                     |
| Agent routing decision    | `decisions.log`| SUCCESS, WARNING, FAIL   |
| Execution start           | `updates.log`  | SUCCESS                  |
| Execution completion      | `updates.log`  | SUCCESS, WARNING         |
| Validation result (pass)  | `updates.log`  | SUCCESS                  |
| Validation result (fail)  | `failures.log` | FAIL                     |
| Failure or block          | `failures.log` | FAIL                     |

Additional moments may be logged as needed. The above are the minimum required set.

---

## 7. FAILURE LOGGING RULE

- Every failure must produce an entry in `failures.log`. No exceptions.
- Silent errors are system violations. If it failed, it must be logged.
- Every failure entry must include the reason in the NOTE field.
- Every failure entry must indicate whether retry is possible.
  - Append `[RETRY: YES]` or `[RETRY: NO]` to the NOTE field.

Example NOTE: `Output failed validation — brand tone violated. [RETRY: YES]`

---

## 8. DECISION TRACEABILITY

- Every routing or strategic decision made by any agent must be logged in `decisions.log`.
- The NOTE field must include short-form reasoning: why this decision was made.
- Decisions must be traceable from input to outcome. A reader must be able to follow the chain.
- Approval, modification, and rejection decisions must each be logged separately.
- "This happened because" must always be answerable from the log.

---

## 9. NON-BLOAT LOGGING RULE

- Logs must be minimal but complete. Every word in a log entry must carry meaning.
- Do not log the same event twice across multiple log files.
- Each log type has one job. Assign entries accordingly.
- Do not add diagnostic information not relevant to the defined fields.
- Do not log intermediate internal states unless they represent a defined logging moment.

---

## 10. LOG STORAGE STRUCTURE

```
/logs/
  updates.log
  decisions.log
  failures.log
  LOGGING-STANDARD.md
  /archive/
    YYYY-MM/
      updates.log
      decisions.log
      failures.log
```

Rules:
- All active logs reside in `/logs/`. No exceptions.
- Logs must not be placed in production output directories.
- Active log files are append-only during normal operation.
- Overwriting an active log requires a controlled rotation event (see Section 11).
- No log file may be silently replaced.

---

## 11. CLEANUP & ROTATION RULE

- Logs are rotated on the first day of each calendar month.
- At rotation: active log files are moved to `/logs/archive/YYYY-MM/`.
- New empty log files are created in `/logs/` after archiving.
- Archived logs are retained for a minimum of 12 months before deletion eligibility.
- Deletion of archived logs requires explicit system owner approval.
- Rotation events must themselves be logged in `updates.log` before the file is moved.
- Log rotation does not alter or truncate log content.

---

## 12. SECURITY & INTEGRITY RULE

- Log entries must not be modified after writing. Append-only.
- No entry may be deleted from an active log without a logged justification entry.
- Controlled deletion requires: timestamp, reason, and system owner authorization recorded in `updates.log`.
- Logs must not contain secrets, credentials, or personally identifiable information.
- Log file permissions must restrict write access to the GENESIS runtime only.
- Integrity can be verified by checking log entry sequence and timestamps for gaps.

---

## 13. HUMAN READABILITY RULE

- Every log entry must be readable by a non-technical human familiar with the system.
- Use plain English in NOTE fields. No codes, abbreviations, or jargon without context.
- The pipe-delimited format is structured but not opaque — fields are labeled.
- Logs must not require a decoder or tool to understand.
- Clarity takes priority over compression. A slightly longer NOTE is acceptable if it removes ambiguity.

---

## 14. EXAMPLES

### Valid `updates.log` entry

```
2026-04-07T23:41:29Z | TASK: TASK-012 | TYPE: UPDATE | AGENT: ContentAgent | ACTION: Execution completed — output file written to /output/task-012.md | RESULT: SUCCESS | NOTE: All modules generated; output passed structure validation on first pass.
```

---

### Valid `decisions.log` entry

```
2026-04-07T23:38:05Z | TASK: TASK-012 | TYPE: DECISION | AGENT: Orchestrator | ACTION: Task routed to ContentAgent | RESULT: SUCCESS | NOTE: Input type classified as long-form insight; ContentAgent assigned per routing protocol.
```

---

### Valid `failures.log` entry

```
2026-04-07T23:45:12Z | TASK: TASK-012 | TYPE: FAILURE | AGENT: ValidationAgent | ACTION: Output rejected — brand tone violation detected | RESULT: FAIL | NOTE: MODULE 2 contained urgency language prohibited by OUTPUT-STANDARD.md Section II. [RETRY: YES]
```

---

## HARD CONSTRAINTS

- No silent execution.
- No missing logs at defined logging moments.
- No mixing log types within a single file.
- No unstructured or partial entries.
- No excessive verbosity in NOTE fields.

---

## FAILURE CONDITIONS

This logging system is INVALID if:

- Actions cannot be traced from input to completion.
- Decisions are absent from `decisions.log`.
- Failures do not appear in `failures.log`.
- Log entries are inconsistent in format or field values.
- Logs become unreadable due to verbosity or format drift.

---

## SUCCESS CRITERIA

This logging system is SUCCESSFUL if:

- Every task can be traced end-to-end using log entries alone.
- System behavior can be analyzed without re-running the system.
- Failures are visible, categorized, and carry retry guidance.
- Decisions are explainable from the NOTE field without additional context.
- Logs remain clean, structured, and human-readable over time.

---

STATUS: Locked as Baseline // 2026 // GENESIS Runtime
