# TASK v1.0 (LOCKED)

## PURPOSE

This document defines how tasks are created, structured, processed, and completed within the GENESIS system.

TASK is the execution unit of the system.

Without a valid task:
- agents have no direction,
- execution becomes random,
- system loses purpose.

Therefore:

No valid task = no execution.

---

## I. CORE PRINCIPLE

Every task must be:

1. Defined
2. Scoped
3. Actionable
4. Traceable
5. Verifiable

If any condition fails:

STATE: BLOCKED

---

## I.1 STATE AND MODE ALIGNMENT

Task processing must follow:

- Task intake → STATE: READY / MODE: ANALYSIS  
- Task execution → STATE: ACTIVE / MODE: EXECUTION or CREATION  
- Task validation → STATE: REVIEW / MODE: REVIEW  
- Task completion → STATE: COMPLETE / MODE: SAFE  

If failure occurs:

STATE: FAILED  
MODE: RECOVERY

---

## II. TASK STRUCTURE

Every task must include:

- TASK_ID: unique identifier
- OBJECTIVE: what must be achieved
- SCOPE: boundaries of execution
- INPUTS: required data sources
- OUTPUTS: expected result
- CONSTRAINTS: rules and limitations
- PRIORITY: (LOW / MEDIUM / HIGH)
- STATUS: current state reference

If any field is missing:
→ STATE: BLOCKED

---

## III. VALID TASK SOURCES

Tasks may originate only from:

### 1. TASKMASTER

Primary task registry.

Rules:
- highest operational authority (after system laws)
- must be treated as structured input

---

### 2. HUMAN OPERATOR

Manually defined tasks.

Requirements:
- must be explicit
- must follow task structure
- must not violate system laws

---

### 3. SYSTEM GENERATED TASKS

Derived tasks created by agents.

Requirements:
- must be linked to parent task
- must define clear purpose
- must not expand scope uncontrollably

---

## IV. TASK VALIDATION

Before execution, every task must pass:

### CHECK 1 — STRUCTURE

All required fields present.

If missing:
→ STATE: BLOCKED

---

### CHECK 2 — CLARITY

Objective must be clear.

If unclear:
→ ANALYSIS → if unresolved → BLOCKED

---

### CHECK 3 — SCOPE CONTROL

Task must define boundaries.

If undefined:
→ STATE: BLOCKED

---

### CHECK 4 — CONSISTENCY

Task must not conflict with:
- system laws
- other tasks
- active workflows

If conflict:
→ STATE: BLOCKED

---

### CHECK 5 — EXECUTABILITY

Task must be realistically executable.

If not:
→ STATE: BLOCKED

---

## V. TASK LIFECYCLE

Every task follows:

1. Created
2. Validated
3. Accepted (READY)
4. Executed (ACTIVE)
5. Reviewed (REVIEW)
6. Completed (COMPLETE)

Error paths:

- Any phase → BLOCKED  
- Execution → FAILED  

---

## VI. TASK PROCESS FLOW

1. Receive task
2. Validate task
3. If invalid → STOP → STATE: BLOCKED
4. If valid → STATE: READY
5. Execute task → STATE: ACTIVE
6. Validate output → STATE: REVIEW
7. If valid → STATE: COMPLETE
8. If invalid → REVIEW or FAILED

---

## VII. TASK LOG FORMAT

Minimum log:

AGENT: [name]  
TASK_ID: [id]  
STATE: [state]  
MODE: [mode]  
ACTION: [short description]  
TIMESTAMP: [YYYY-MM-DD HH:MM UTC]  
RESULT: [success/failure]

---

## VIII. TASK PRIORITY

Tasks must be handled based on:

1. System-critical tasks
2. High priority tasks
3. Medium priority tasks
4. Low priority tasks

If conflict:
- higher priority overrides
- lower priority delayed or paused

---

## IX. TASK LIMITATIONS

Tasks must not:

- violate system laws
- modify unrelated components
- create uncontrolled dependencies
- execute without validated input
- complete without validated output

If detected:
→ STATE: BLOCKED or FAILED

---

## X. FINAL STANDARD

A system without task control is not a system.

If tasks are controlled:
- execution becomes deterministic
- agents become reliable
- system scales

If tasks are uncontrolled:
- system becomes chaotic

Therefore:

TASK STRUCTURE = SYSTEM EXECUTION
