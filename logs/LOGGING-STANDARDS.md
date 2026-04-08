# LOGGING STANDARDS — GENESIS SYSTEM

**Version:** 1.0  
**Status:** Active  
**Scope:** All agents, workflows, and human operators  
**Alignment:** GENESIS-LAWS.md, TASKMASTER.md  

---

## 1. PURPOSE

Logging is a system requirement. It is not optional and not stylistic.

**Why logging exists:**
- GENESIS executes tasks across multiple agents sequentially and in parallel. Without structured logs, no authoritative record exists for what happened, when, or why.
- Silent failures compound. An unlogged failure is an invisible failure. Invisible failures become systemic drift.
- Every agent action must be auditable. A system that cannot explain itself cannot be trusted, debugged, or improved.
- Human review depends on log accuracy. Logs are the primary source of truth for system oversight.

**What logging must provide:**
- Traceability: every task can be followed from input to completion or failure.
- Auditability: every decision is recorded with its reason.
- Debuggability: every failure is visible, categorized, and carries enough context for diagnosis.
- Human review: logs are readable without tools or decoding.

**What logging prevents:**
- Re-execution of tasks whose prior state is unknown.
- Validation failures passing downstream undetected.
- Loss of execution context between agent handoffs.
- Ambiguity about who did what and when.

---

## 2. SCOPE

This standard governs the following log files:

| File | Role |
|------|------|
| `logs/updates.log` | Record of completed actions and real state changes |
| `logs/failures.log` | Record of errors, blocked operations, and failed validations |
| `logs/decisions.log` | Record of approved decisions and operational direction changes |
| `logs/bridge-sync.log` | Record of product bridge state across outputs, preview, and storefront |
| `logs/integrity.log` | Record of ecological preservation audit status and human-review flags |

No other log files are authorized without a GENESIS-LAWS-aligned decision recorded in `decisions.log`.

---

## 3. UNIVERSAL ENTRY FORMAT

Every log entry across all four files must follow this exact structure:

```
[YYYY-MM-DDTHH:MM:SSZ] | SOURCE: <source> | ACTION: <action> | TARGET: <target> | STATUS: <status> | DETAIL: <detail>
```

**Field definitions:**

| Field | Description |
|-------|-------------|
| Timestamp | ISO 8601 UTC. Format: `YYYY-MM-DDTHH:MM:SSZ`. Required. |
| SOURCE | The agent, workflow, or human operator that produced the entry. |
| ACTION | A short verb phrase describing what occurred. Past tense. |
| TARGET | The file, task ID, product, or system component affected. |
| STATUS | One of the allowed status values defined in Section 4. |
| DETAIL | One sentence. Specific. No narrative. No vague language. |

**Constraints:**
- All fields are mandatory. No field may be empty or omitted.
- DETAIL must be a single sentence. No multi-line values.
- Each entry occupies exactly one line.
- Entries are written in plain text. No markdown, no nested structures.
- Entries are appended only. No in-place modification of existing entries.

---

## 4. STATUS VALUES

Only the following status values are permitted. No freeform status text is allowed.

| Status | When to use |
|--------|-------------|
| `SUCCESS` | Action completed as expected. State changed as intended. |
| `FAILED` | Action could not be completed. Reason must appear in DETAIL. |
| `PENDING` | Action is queued or awaiting a prerequisite. |
| `SKIPPED` | Action was intentionally bypassed with a recorded reason. |
| `REVIEW_REQUIRED` | Action completed but outcome requires human inspection before proceeding. |
| `BLOCKED` | Action cannot proceed due to a missing dependency, failed validation, or system constraint. |

---

## 5. WRITING RULES

Every log entry must comply with the following rules without exception.

**Language:**
- No emotional language. No: "unfortunately", "sadly", "finally", "great news".
- No vague wording. No: "something went wrong", "updated some files", "checked things".
- No first-person voice. No: "I have completed", "we are now ready".
- Use plain, precise English.

**Structure:**
- One event = one entry. Do not combine multiple actions into a single entry.
- No narrative paragraphs. DETAIL is one sentence, not a summary.
- No duplicate entries for the same event unless the status changed. If status changes, a new entry is required.
- No speculative entries. Log what happened, not what was intended.

**Content:**
- Logs must reflect reality. Do not log expected outcomes as completed actions.
- Log the actual state, not the desired state.
- If an action was blocked or skipped, record why — not what was hoped for.

---

## 6. FILE-SPECIFIC STANDARDS

---

### `updates.log`

**Purpose:** Record of real state changes and completed system actions.

**May contain:**
- Completed task executions
- File creation, modification, or deletion
- System state changes
- Workflow completions and handoffs
- Log rotation events

**Must not contain:**
- Failures or errors (use `failures.log`)
- Decisions or routing choices (use `decisions.log`)
- Bridge or product sync state (use `bridge-sync.log`)
- Planned or intended actions that have not yet occurred

**Required format:**
```
[TIMESTAMP] | SOURCE: <agent or human> | ACTION: <completed action> | TARGET: <file or task ID> | STATUS: SUCCESS | DETAIL: <one sentence, factual>
```

**Authorized writers:** TASK-EXECUTOR, GENESIS-ORCHESTRATOR, human operator, workflow runner.

---

### `failures.log`

**Purpose:** Record of every point where the system could not proceed as expected.

**May contain:**
- Validation failures
- Runtime errors
- Blocked executions
- Missing files or missing required inputs
- Failed link checks, broken paths, or 404-producing references
- Outputs that failed quality or standard checks

**Must not contain:**
- Successful actions (use `updates.log`)
- Decisions or routing logic (use `decisions.log`)
- General progress notes

**Required format:**
```
[TIMESTAMP] | SOURCE: <agent or human> | ACTION: <what failed> | TARGET: <file, task ID, or path> | STATUS: FAILED | DETAIL: <reason for failure. RETRY: YES|NO>
```

Every failure entry must include `RETRY: YES` or `RETRY: NO` at the end of the DETAIL field.

**Authorized writers:** OUTPUT-VALIDATOR, TASK-EXECUTOR, GENESIS-ORCHESTRATOR, human operator, workflow runner.

---

### `decisions.log`

**Purpose:** Record of approved structural or operational decisions.

**May contain:**
- Routing decisions (which agent received which task)
- Human-approved direction changes
- Approve, modify, or reject outcomes from validation
- Strategic choices with system-level impact
- Branching logic triggered by defined conditions

**Must not contain:**
- Task execution updates (use `updates.log`)
- Failures (use `failures.log`)
- Decisions made without human approval when human approval is required per GENESIS-LAWS.md

**Required format:**
```
[TIMESTAMP] | SOURCE: <agent or human> | ACTION: <decision made> | TARGET: <task ID or system component> | STATUS: SUCCESS | DETAIL: <reason for decision. Approved by: <human|system-rule>>
```

Every decision entry must state whether it was approved by a human or triggered autonomously by a defined system rule.

**Authorized writers:** GENESIS-ORCHESTRATOR, OUTPUT-VALIDATOR, human operator.

---

### `bridge-sync.log`

**Purpose:** Record of product bridge state between outputs, preview, and storefront readiness.

**May contain:**
- Status of output files (PDF, Gumroad copy, preview HTML) relative to current product state
- Preview URL validity checks
- Storefront readiness checks (product listed, link valid, price set)
- Sync gaps between what exists in outputs/ and what is live or accessible
- Manual sync confirmations by human operator

**Must not contain:**
- General task updates (use `updates.log`)
- Failures unrelated to the product bridge pipeline (use `failures.log`)
- Decisions about product direction (use `decisions.log`)

**Required format:**
```
[TIMESTAMP] | SOURCE: <agent or human> | ACTION: <sync action or check> | TARGET: <product name or file path> | STATUS: <status> | DETAIL: <state of bridge: what matches, what is missing, what is pending>
```

**Authorized writers:** TASK-EXECUTOR, GENESIS-ORCHESTRATOR, human operator, workflow runner.

---

## 7. TIMESTAMP RULES

- All timestamps use ISO 8601 UTC format: `YYYY-MM-DDTHH:MM:SSZ`
- Example: `2026-04-08T06:35:00Z`
- No local timezone offsets. UTC only.
- No entry may be written without a timestamp.
- Entries within each log file are ordered chronologically, oldest first.
- No retroactive timestamp modification is permitted under any condition.

---

## 8. RETENTION AND CLEANLINESS RULES

**Retention:**
- Log files are append-only during normal operation.
- No log file may be deleted without explicit human approval.
- No log entry may be removed from an active log without a justification entry appended immediately after.
- If a deletion or correction is required, append a correction entry — do not modify or hide the original.

**Corrections:**
- Incorrect entries must be followed by a correction entry. Format:
  ```
  [TIMESTAMP] | SOURCE: <source> | ACTION: Correction applied to prior entry | TARGET: <log file and approximate timestamp of original> | STATUS: REVIEW_REQUIRED | DETAIL: <what was wrong and what the correct state is>
  ```

**Cleanliness:**
- Log files must not grow into unreadable volumes. Rotate on the first day of each calendar month.
- At rotation: active logs are moved to `logs/archive/YYYY-MM/`. New empty files are created.
- Archived logs are retained for a minimum of 12 months.
- Deletion of archived logs requires human approval logged in `decisions.log`.
- Log rotation events must be recorded in `updates.log` before the file is moved.

**Prohibited:**
- Rewriting history silently.
- Deleting entries to hide system failures.
- Truncating logs without a rotation event.
- Substituting a new file for an existing log without a logged rotation.

---

## 9. EXAMPLE ENTRIES

### `updates.log` examples

```
2026-04-08T06:10:00Z | SOURCE: TASK-EXECUTOR | ACTION: File created | TARGET: outputs/pdf/money-program-reset.pdf | STATUS: SUCCESS | DETAIL: PDF generated from MONEY-PROGRAM-RESET.md and written to outputs/pdf/.
```

```
2026-04-08T06:15:30Z | SOURCE: GENESIS-ORCHESTRATOR | ACTION: Task assigned | TARGET: TASK-012 | STATUS: SUCCESS | DETAIL: Task routed to TASK-EXECUTOR per TASKMASTER.md execution order.
```

```
2026-04-08T06:22:44Z | SOURCE: workflow-runner | ACTION: Log rotation completed | TARGET: logs/updates.log | STATUS: SUCCESS | DETAIL: Active log archived to logs/archive/2026-04/ before new empty file created.
```

```
2026-04-08T06:30:00Z | SOURCE: human | ACTION: Preview confirmed live | TARGET: preview/money-program-reset.html | STATUS: SUCCESS | DETAIL: Preview URL verified accessible at https://aurinbeyond.github.io/Genesis/preview/money-program-reset.html.
```

---

### `failures.log` examples

```
2026-04-08T06:11:05Z | SOURCE: OUTPUT-VALIDATOR | ACTION: Output rejected — structure violation | TARGET: outputs/gumroad/money-program-reset.md | STATUS: FAILED | DETAIL: Required section "PRICE" missing from Gumroad copy. RETRY: YES
```

```
2026-04-08T06:14:22Z | SOURCE: TASK-EXECUTOR | ACTION: File not found | TARGET: core/core.html | STATUS: BLOCKED | DETAIL: ARKANA-OS flow requires core.html — file does not exist. RETRY: NO
```

```
2026-04-08T06:18:55Z | SOURCE: workflow-runner | ACTION: Link validation failed | TARGET: offer.html CTA button | STATUS: FAILED | DETAIL: CTA links to https://aurinbeyond.gumroad.com/l/product-slug — slug not verified as active. RETRY: YES
```

```
2026-04-08T06:25:11Z | SOURCE: OUTPUT-VALIDATOR | ACTION: Gumroad description rejected | TARGET: outputs/gumroad/product-001.md | STATUS: FAILED | DETAIL: Description contains urgency language prohibited by OUTPUT-STANDARD.md Section II. RETRY: YES
```

```
2026-04-08T06:31:00Z | SOURCE: GENESIS-ORCHESTRATOR | ACTION: Task blocked — dependency unresolved | TARGET: TASK-015 | STATUS: BLOCKED | DETAIL: TASK-015 requires PDF to exist in outputs/pdf/ — PDF not yet generated. RETRY: NO
```

---

### `decisions.log` examples

```
2026-04-08T06:09:00Z | SOURCE: GENESIS-ORCHESTRATOR | ACTION: Task routed to TASK-EXECUTOR | TARGET: TASK-012 | STATUS: SUCCESS | DETAIL: Input classified as output generation task per INPUT.md routing rules. Approved by: system-rule
```

```
2026-04-08T06:20:00Z | SOURCE: human | ACTION: CSS architecture decision locked | TARGET: style.css (root) | STATUS: SUCCESS | DETAIL: Root style.css retained as primary stylesheet; assets/css/style.css deprecated. Approved by: human
```

```
2026-04-08T06:28:00Z | SOURCE: OUTPUT-VALIDATOR | ACTION: Output modification approved | TARGET: outputs/gumroad/product-001.md | STATUS: SUCCESS | DETAIL: Minor title adjustment accepted; does not alter product intent or pricing. Approved by: human
```

```
2026-04-08T06:33:00Z | SOURCE: human | ACTION: Gumroad base URL standard confirmed | TARGET: all outbound Gumroad links | STATUS: SUCCESS | DETAIL: Only https://aurinbeyond.gumroad.com/ permitted until product slugs are verified. Approved by: human
```

---

### `bridge-sync.log` examples

```
2026-04-08T06:12:00Z | SOURCE: TASK-EXECUTOR | ACTION: Bridge sync initiated | TARGET: money-program-reset | STATUS: PENDING | DETAIL: PDF and Gumroad copy exist in outputs/; preview HTML not yet generated.
```

```
2026-04-08T06:16:00Z | SOURCE: TASK-EXECUTOR | ACTION: Preview file created | TARGET: preview/money-program-reset.html | STATUS: SUCCESS | DETAIL: Preview HTML written; bridge state updated from PENDING to REVIEW_REQUIRED.
```

```
2026-04-08T06:26:00Z | SOURCE: human | ACTION: Storefront readiness check performed | TARGET: aurinbeyond.gumroad.com | STATUS: REVIEW_REQUIRED | DETAIL: Product not yet published on Gumroad; PDF link cannot be verified until listing is live.
```

```
2026-04-08T06:32:00Z | SOURCE: GENESIS-ORCHESTRATOR | ACTION: Bridge sync gap logged | TARGET: product-001 | STATUS: BLOCKED | DETAIL: outputs/pdf/the-source-within.pdf does not exist; Gumroad delivery cannot proceed until file is generated.
```

```
2026-04-08T06:40:00Z | SOURCE: human | ACTION: Full bridge confirmed | TARGET: money-program-reset | STATUS: SUCCESS | DETAIL: PDF, Gumroad copy, preview HTML, and storefront listing all verified; bridge state is READY.
```

---

## 10. ALIGNMENT

This standard operates under and must not conflict with:

- **GENESIS-LAWS.md** — top-level system law. Human authority is final. No action goes live without human approval where required. Logs must support this by recording who approved what.
- **TASKMASTER.md** — task execution protocol. Every task lifecycle event (assignment, execution, completion, failure) must produce a log entry in the appropriate file.
- **Human review logic** — logs are the primary input for human oversight. They must be accurate, structured, and readable without requiring system access.
- **System integrity** — logs are append-only. History must not be altered. The log is not a workspace — it is a record.

---

## HARD CONSTRAINTS

- No silent execution. If it happened, it is logged.
- No freeform status values. Use only the values defined in Section 4.
- No mixed log files. Each file has one purpose. Do not cross-post entries.
- No unstructured or partial entries. All fields are mandatory.
- No emotional or vague language in any field.
- No log deletion without human approval and a justification entry.
- No rewriting history. Corrections are appended, not substituted.

---

## FAILURE CONDITIONS

This standard is violated if:

- Any executed task has no corresponding entry in `updates.log`.
- Any failure has no entry in `failures.log`.
- Any decision has no entry in `decisions.log`.
- Bridge state changes have no entry in `bridge-sync.log`.
- Any entry is missing a field, uses a non-standard status, or spans multiple lines.
- A log file has been modified in-place rather than appended to.

---

STATUS: Active — GENESIS System // 2026
