# STATE v1.0 (LOCKED)

## PURPOSE

This document defines all valid system states for GENESIS and its mini-agents.

It exists to ensure that every agent:
- knows its current condition,
- behaves according to that condition,
- does not act outside its allowed operational state,
- and can be audited clearly by both humans and other agents.

State is not decoration.  
State controls permission, readiness, execution, and recovery.

---

## I. CORE PRINCIPLE

Every agent must always be in one clearly defined state.

No agent may operate in:
- multiple states at once,
- an undefined state,
- or a self-invented state.

If state is unclear, the agent must default to:

STATE: BLOCKED

until the condition is verified.

---

## II. VALID SYSTEM STATES

### 1. IDLE

Meaning:  
The agent is available but has no active task.

Allowed actions:
- read system files
- wait for instructions
- validate readiness
- report availability

Not allowed:
- executing tasks
- modifying files
- producing final outputs as if a task were active

---

### 2. READY

Meaning:  
The agent has validated required conditions and is prepared to begin work.

Required conditions:
- relevant task exists
- required files are accessible
- scope is defined
- no blocking conflict is present

Allowed actions:
- prepare execution
- confirm dependencies
- move to active state

Not allowed:
- skipping into uncontrolled execution
- changing unrelated files
- acting outside assigned scope

---

### 3. ACTIVE

Meaning:  
The agent is currently performing its assigned task.

Allowed actions:
- execute the defined task
- write or modify approved outputs
- update logs
- complete one scoped action at a time

Required behavior:
- stay within task boundaries
- preserve system rules
- avoid side actions
- keep outputs deterministic and auditable

Not allowed:
- starting unrelated tasks
- inventing new objectives
- modifying system law files unless explicitly assigned

---

### 4. REVIEW

Meaning:  
Execution is complete, but the result must be checked before closure.

Allowed actions:
- validate output
- run structural checks
- verify alignment with laws, scope, and task intent
- prepare result for approval

Not allowed:
- skipping validation
- endless modification loops
- changing task scope during review

---

### 5. COMPLETE

Meaning:  
The task has been executed, verified, and closed correctly.

Allowed actions:
- mark completion
- log final state
- return to IDLE

Required conditions:
- output exists
- validation passed
- task closure is documented
- no unresolved blocker remains

Not allowed:
- reopening without new trigger
- false completion

---

### 6. BLOCKED

Meaning:  
The agent cannot continue because a required condition is missing or invalid.

Examples:
- missing file
- invalid scope
- permissions issue
- conflicting instructions
- system law violation risk
- dependency failure

Allowed actions:
- stop execution
- report blocker
- log exact reason
- wait for resolution

Not allowed:
- guessing
- bypassing constraints
- forcing progress

---

### 7. FAILED

Meaning:  
Execution was attempted but ended in failure.

Examples:
- write failed
- validation failed
- corrupted output
- runtime error

Allowed actions:
- stop
- log failure
- preserve evidence
- prepare recovery

Not allowed:
- hiding failure
- presenting partial output as success
- uncontrolled retry

---

### 8. ARCHIVED

Meaning:  
Inactive but preserved for history and audit.

Allowed actions:
- remain readable
- support audit or rollback

Not allowed:
- acting as active truth unless restored

---

## III. STATE TRANSITIONS

Valid transitions:

- IDLE → READY
- READY → ACTIVE
- ACTIVE → REVIEW
- REVIEW → COMPLETE
- COMPLETE → IDLE

Error paths:

- READY → BLOCKED
- ACTIVE → BLOCKED
- ACTIVE → FAILED
- REVIEW → BLOCKED
- REVIEW → FAILED
- FAILED → READY (after correction)
- BLOCKED → READY (after resolution)

Archive paths:

- COMPLETE → ARCHIVED
- FAILED → ARCHIVED
- BLOCKED → ARCHIVED

Forbidden:

- IDLE → COMPLETE
- READY → COMPLETE
- BLOCKED → ACTIVE
- FAILED → COMPLETE

---

## IV. STATE RULES

RULE 1 — SINGLE SOURCE OF TRUTH  
State must always be explicit.

RULE 2 — NO SILENT TRANSITIONS  
Every change must be logged.

RULE 3 — NO EXECUTION IN BLOCKED OR FAILED  
Execution is strictly prohibited.

RULE 4 — REVIEW BEFORE COMPLETE  
No direct ACTIVE → COMPLETE.

RULE 5 — STATE DEFINES PERMISSION  
Behavior follows state, not intent.

RULE 6 — WHEN IN DOUBT, BLOCK  
Uncertainty = BLOCKED.

---

## V. MINIMUM STATE LOG FORMAT

AGENT: [agent-name]  
TASK: [task-id]  
PREVIOUS_STATE: [state]  
CURRENT_STATE: [state]  
TIMESTAMP: [YYYY-MM-DD HH:MM UTC]  
REASON: [factual explanation]

Example:

AGENT: AGENT-COURSE-CREATOR  
TASK: Build module structure  
PREVIOUS_STATE: READY  
CURRENT_STATE: ACTIVE  
TIMESTAMP: 2026-04-06 20:14 UTC  
REASON: Validation complete, execution started

---

## VI. HUMAN OVERRIDE

Human override is allowed but must:
- be explicit
- be logged
- be treated as authoritative

---

## VII. FAILURE DISCIPLINE

On FAILED, report:
1. what failed
2. where
3. why (if known)
4. retry possibility

No emotional language.

---

## VIII. BLOCKER DISCIPLINE

On BLOCKED, report:
1. exact blocker
2. affected dependency
3. internal/external
4. condition for READY

---

## IX. OUTPUT REQUIREMENT

All agents must be state-aware:
- state must be identifiable
- transitions must be valid
- invalid states rejected

---

## X. FINAL STANDARD

A stable system is defined by controlled state.

If state is clear:
- execution is reliable
- errors are traceable
- scaling is possible

If state is unclear:
- the system becomes noise

NO STATE CLARITY = NO SYSTEM INTEGRITY
