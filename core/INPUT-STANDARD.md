# INPUT STANDARD v1.0
# AurinBeyond / Genesis — Execution Layer
# Status: ACTIVE

---

## PURPOSE

This document defines the required structure for all task input in the GENESIS system.

The runtime reads tasks from `TASKMASTER.md`. Every task must conform to this standard before execution is permitted.

**No structured input = no execution.**

---

## I. TASK ENTRY FORMAT

Tasks are defined in `TASKMASTER.md` under the `## ACTIVE TASKS` section.

Each task uses the following checkbox format:

```
- [ ] TASK-ID: Task Title [TYPE: task-type] [GOAL: short goal] [PRIORITY: high|medium|low]
```

**Minimum required fields in each task line:**
- `TASK-ID` — unique identifier (e.g., `TASK-002`)
- `Task Title` — clear, human-readable name
- `[TYPE: ...]` — task classification (see Section II)
- `[GOAL: ...]` — one-line statement of the intended output
- `[PRIORITY: ...]` — `high`, `medium`, or `low`

**Example:**
```
- [ ] TASK-002: Create Gumroad sales page for first offer [TYPE: page-structure] [GOAL: produce complete sales page copy] [PRIORITY: high]
```

---

## II. TASK TYPE REGISTRY

The `TYPE` field determines which agents are activated. Only registered task types are valid.

| Type | Description | Agents Activated |
|---|---|---|
| `offer-creation` | Define a new product or offer | System Orchestrator → Offer Architect |
| `funnel-design` | Create a conversion funnel | Funnel Architect |
| `raw-copy` | Produce unrefined content | Content Producer |
| `voice-refinement` | Align copy to brand voice | Humanizer |
| `brand-validation` | Validate output against brand rules | Brand Guardian |
| `page-structure` | Build a complete page structure | Genesis Architect |
| `authority-content` | Long-form brand authority piece | Frequency Transmitter |
| `legal-compliance` | Privacy policy, terms, disclaimers | Legal & Compliance Guard |
| `chat-interaction` | Real-time user communication | Semantic Core → Chat Agent → Language Polisher |
| `system-task` | Internal system operation | System Orchestrator |

Tasks with unregistered types are flagged as `INVALID` and execution is blocked.

---

## III. INPUT VALIDATION RULES

Before execution begins, the runtime validates the following:

### Required conditions (ALL must pass)

| Condition | Pass | Fail action |
|---|---|---|
| Task line exists in ACTIVE TASKS | Line found | Block execution, log to `failures.log` |
| Task status is unchecked `[ ]` | Not yet completed | Skip task, find next valid task |
| TASK-ID is present | `TASK-XXX` format | Block execution |
| Task title is non-empty | Text present | Block execution |
| TYPE field is present | `[TYPE: ...]` found | Block execution |
| TYPE value is in registry | Matches known type | Block execution |
| PRIORITY field is present | `[PRIORITY: ...]` found | Proceed with default `medium` |
| Core files exist | All files in `core/` verify list | Block execution |

### If any required condition fails:
1. Execution halts immediately
2. An entry is appended to `logs/failures.log`
3. No agent executes
4. No files are modified
5. The GitHub Actions run reports failure visibly

---

## IV. EXTENDED TASK CONTEXT (OPTIONAL)

For complex tasks, extended context can be provided in `core/TASK.md`.

Extended context format:
```
# TASK: TASK-ID

## Title
[Task title]

## Goal
[What this task must produce]

## Context
[Background information, existing assets, constraints]

## Requested Output
[Exact output format and location expected]

## Constraints
[Brand rules, format limits, scope limits]

## Target Agent(s)
[Optional: specify which agent(s) to prioritize]
```

If `core/TASK.md` is present and contains context for the current task, it is loaded and passed to the active agents. It does not replace the task line in `TASKMASTER.md` — both are required.

---

## V. INPUT REJECTION PROTOCOL

If input is rejected, the following occurs:

1. `logs/failures.log` receives a structured entry:
   ```
   [YYYY-MM-DD HH:MM] TASK-ID → failure: input rejected — reason: [reason] — state: BLOCKED (GENESIS-RUNTIME)
   ```

2. The GitHub Actions run exits as failed.

3. No partial output is written.

4. Source is notified via the failed run status in GitHub Actions.

5. To resume, Source must correct the input in `TASKMASTER.md` or `core/TASK.md` and re-trigger the workflow.

---

## VI. INPUT IMMUTABILITY RULE

Once a task has been executed and marked complete (`[x]`):
- Its entry in `TASKMASTER.md` must not be edited or reverted
- New tasks must be added as new entries
- Completed tasks serve as the audit history of the system

---

**This standard is locked. Changes require a version bump in the file header.**
