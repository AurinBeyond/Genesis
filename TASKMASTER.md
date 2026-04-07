# GENESIS TASKMASTER v3.0

> **STATUS:** ACTIVE
> **CONTROL:** SOURCE (user approval required before each step advances and before DONE)
> **SYSTEM:** GENESIS-AI-AGENT

---

## ACTIVE TASK

| Field | Value |
|---|---|
| ID | TASK-001 |
| Agent | FUNNEL-ARCHITECT |
| Status | REVIEW |
| current_step | 2 |
| next_agent | CONTENT-PRODUCER |
| total_steps | 5 |

**Step 2 output:** `logs/outputs/TASK-001/02-funnel.md` — awaiting Source approval before Step 3 starts.

---

## REVIEW QUEUE

Tasks/steps completed by agent — awaiting Source approval before next step runs.

| ID | Step | Agent | Output | Status |
|---|---|---|---|---|
| TASK-001 | 1 | OFFER-ARCHITECT | logs/outputs/TASK-001/01-offer.md | APPROVED |
| TASK-001 | 2 | FUNNEL-ARCHITECT | logs/outputs/TASK-001/02-funnel.md | REVIEW |

---

## COMPLETED TASKS

Tasks approved by Source (all steps done).

| ID | Agent | Task | Approved |
|---|---|---|---|
| TASK-000 | SYSTEM | Setup core repository and documentation | yes |

---

## PIPELINE STEPS

Every task runs through this 5-step pipeline:

| Step | Agent | Output File | Action |
|---|---|---|---|
| 1 | OFFER-ARCHITECT | 01-offer.md | Define product |
| 2 | FUNNEL-ARCHITECT | 02-funnel.md | Define sales flow |
| 3 | CONTENT-PRODUCER | 03-content.md | Write raw copy |
| 4 | HUMANIZER | 04-humanized.md | Rewrite in human voice |
| 5 | BRAND-GUARDIAN | FINAL.md | Validate + assemble final |

Each step requires Source approval before the next begins.

---

## CONTROL RULES

1. Agent executes its assigned step and saves output to `logs/outputs/TASK-XXX/NN-step.md`.
2. Agent logs action to `logs/updates.log` with timestamp and step number.
3. Agent sets Status to `REVIEW` — never `DONE`.
4. Agent must not overwrite an existing step file.
5. Only Source approves each step and triggers the next agent.
6. Only Source (user) moves task from REVIEW → DONE after FINAL.md is complete.
7. No agent skips steps. No agent writes to a future step file.

---

## HOW TO ADVANCE A STEP (Source only)

After reviewing a step output:
1. Update `current_step` to the next number in the ACTIVE TASK table.
2. Update `next_agent` to the next agent in the pipeline.
3. Add the next agent's task to the ACTIVE TASK table with status `pending`.
4. Agent will execute on next run.

---

**Source is internal. Control remains with you.**
