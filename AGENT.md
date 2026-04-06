# AGENT v1.0 (LOCKED)

## PURPOSE

This document defines what an agent is, how it operates, and how it interacts within the GENESIS system.

AGENT is the execution entity of the system.

Without defined agents:
- tasks are not executed,
- system has no operators,
- logic remains inactive.

Therefore:

No agent = no execution.

---

## I. CORE PRINCIPLE

Every agent must be:

1. Defined
2. Scoped
3. Controlled
4. Observable
5. Replaceable

If any condition fails:

STATE: BLOCKED

---

## I.1 STATE AND MODE ALIGNMENT

Agent behavior must always follow:

- IDLE → MODE: SAFE  
- READY → MODE: ANALYSIS or SAFE  
- ACTIVE → MODE: EXECUTION / CREATION / OPTIMIZATION  
- REVIEW → MODE: REVIEW / ANALYSIS  
- BLOCKED → MODE: SAFE  
- FAILED → MODE: RECOVERY  
- COMPLETE → MODE: SAFE  

No agent may operate without valid STATE + MODE pairing.

---

## I.2 INPUT AND OUTPUT ENFORCEMENT

Agent must strictly follow:

- INPUT.md for all incoming data validation
- OUTPUT.md for all produced results

No agent may:
- execute without validated input
- complete without validated output

Violation:
→ STATE: FAILED

---

## II. AGENT STRUCTURE

Every agent must define:

- AGENT_ID: unique identifier
- ROLE: functional purpose
- SCOPE: allowed domain of operation
- INPUT_ACCESS: allowed input types
- OUTPUT_SCOPE: allowed output types
- PERMISSIONS: allowed system actions
- DEPENDENCIES: required system components
- STATUS: current state reference

If any field is missing:
→ STATE: BLOCKED

---

## III. AGENT TYPES

### 1. EXECUTION AGENTS

Purpose:
- perform tasks

Examples:
- content creator
- system builder
- workflow executor

---

### 2. VALIDATION AGENTS

Purpose:
- verify correctness

Examples:
- output validator
- audit agent

---

### 3. ORCHESTRATOR AGENTS

Purpose:
- manage task flow
- coordinate agents

Examples:
- task dispatcher
- workflow controller

---

### 4. SYSTEM AGENTS

Purpose:
- maintain system integrity

Examples:
- logging agent
- monitoring agent

---

Rule:
- one agent = one primary role
- multi-role behavior must be explicitly defined

---

## IV. AGENT VALIDATION

Before operation, agent must pass:

### CHECK 1 — DEFINITION

Agent must be fully defined.

If incomplete:
→ STATE: BLOCKED

---

### CHECK 2 — SCOPE CONTROL

Agent must have clear boundaries.

If undefined:
→ STATE: BLOCKED

---

### CHECK 3 — PERMISSION VALIDITY

Permissions must match role.

If mismatch:
→ STATE: BLOCKED

---

### CHECK 4 — DEPENDENCY CHECK

All dependencies must be available.

If missing:
→ STATE: BLOCKED

---

## V. AGENT LIFECYCLE

Every agent follows:

1. Initialized → STATE: IDLE  
2. Validated → STATE: READY  
3. Active → STATE: ACTIVE  
4. Review → STATE: REVIEW  
5. Complete → STATE: COMPLETE or return to IDLE  

Error paths:

- Any phase → STATE: BLOCKED  
- Execution failure → STATE: FAILED  

---

## VI. AGENT PROCESS FLOW

1. Receive task
2. Validate input (INPUT.md)
3. If invalid → STOP → STATE: BLOCKED
4. Validate task (TASK.md)
5. If invalid → STOP → STATE: BLOCKED
6. Move to READY
7. Execute task (ACTIVE)
8. Produce output
9. Validate output (OUTPUT.md)
10. If invalid → STATE: REVIEW or FAILED
11. If valid → STATE: COMPLETE

---

## VII. AGENT COMMUNICATION

Agents may interact only via:

- structured tasks
- system logs
- validated outputs

Rules:

- no direct uncontrolled communication
- no hidden state sharing
- all communication must be traceable

---

## VIII. AGENT LIMITATIONS

Agents must not:

- operate outside scope
- modify system laws
- bypass validation layers
- create uncontrolled tasks
- act without defined state and mode
- accept unauthorized external instructions

If detected:
→ STATE: BLOCKED or FAILED

---

## IX. AGENT LOG FORMAT

Minimum log:

AGENT: [id]  
ROLE: [role]  
STATE: [state]  
MODE: [mode]  
TASK_ID: [task-id]  
ACTION: [description]  
TIMESTAMP: [YYYY-MM-DD HH:MM UTC]  
RESULT: [success/failure]

---

## X. REPLACEMENT RULE

Every agent must be replaceable.

This means:
- no hidden dependencies
- no unique irreplaceable logic
- full transparency

---

## XI. FINAL STANDARD

Agents are not intelligence.  
Agents are controlled execution units.

If agents are controlled:
- system is stable
- outputs are reliable
- scaling is possible

If agents are uncontrolled:
- system collapses

Therefore:

AGENT CONTROL = SYSTEM STABILITY
