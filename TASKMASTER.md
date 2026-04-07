# GENESIS TASKMASTER v2.0

> **STATUS:** ACTIVE
> **CONTROL:** SOURCE (user approval required before DONE)
> **SYSTEM:** GENESIS-AI-AGENT

---

## ACTIVE TASK

| Field | Value |
|---|---|
| ID | TASK-001 |
| Agent | OFFER-ARCHITECT |
| Task | Define the first sellable product for Gumroad |
| Status | REVIEW |

---

## REVIEW QUEUE

Tasks completed by agent — awaiting Source approval before moving to DONE.

| ID | Agent | Task | Output |
|---|---|---|---|
| TASK-001 | OFFER-ARCHITECT | Define first Gumroad product | logs/outputs/TASK-001.md |

---

## COMPLETED TASKS

Tasks approved by Source.

| ID | Agent | Task | Approved |
|---|---|---|---|
| TASK-000 | SYSTEM | Setup core repository and documentation | yes |

---

## CONTROL RULES

1. Agent executes task and saves output to `logs/outputs/TASK-XXX.md`.
2. Agent logs action to `logs/updates.log` with timestamp.
3. Agent sets task Status to `REVIEW` — never `DONE`.
4. Agent must not overwrite an existing output file.
5. Only Source (user) moves task from REVIEW → DONE.
6. Only Source (user) adds new tasks to ACTIVE TASK.

---

## HOW TO ADD A TASK (Source only)

Replace the ACTIVE TASK table with:

```
| ID | TASK-XXX |
| Agent | AGENT-NAME |
| Task | Description of what to do |
| Status | pending |
```

Agent will pick it up on next run.

---

**Source is internal. Control remains with you.**
