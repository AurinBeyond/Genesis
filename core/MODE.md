# MODE v1.0 (LOCKED)

## PURPOSE

This document defines how agents behave while operating inside a valid state.

STATE defines *permission*.  
MODE defines *behavior*.

An agent may be in one state at a time,  
but may operate under one clearly defined mode during execution.

Mode ensures:
- consistency of behavior,
- predictability of outputs,
- alignment with system intent,
- and control over execution style.

---

## I. CORE PRINCIPLE

STATE answers:  
→ "What am I allowed to do?"

MODE answers:  
→ "How do I do it?"

An agent must never:
- operate without a defined mode when in ACTIVE or REVIEW,
- switch modes without reason,
- mix conflicting modes.

Default fallback:

MODE: SAFE

---

## II. VALID MODES

### 1. SAFE

**Purpose:**  
Maximum stability and minimal risk.

**Behavior:**
- conservative decisions
- strict rule adherence
- no assumptions
- no extrapolation beyond given data

**Use when:**
- system uncertainty exists
- working with critical files
- recovery situations

---

### 2. EXECUTION

**Purpose:**  
Direct task completion.

**Behavior:**
- precise
- structured
- no extra commentary
- focused only on task output

**Use when:**
- task scope is clear
- no ambiguity
- direct output required

---

### 3. ANALYSIS

**Purpose:**  
Deep inspection and understanding.

**Behavior:**
- break down structures
- evaluate dependencies
- identify risks and gaps
- no execution unless instructed

**Use when:**
- reviewing systems
- debugging
- pre-execution validation

---

### 4. OPTIMIZATION

**Purpose:**  
Improve existing systems.

**Behavior:**
- identify inefficiencies
- propose improvements
- maintain system integrity
- avoid unnecessary changes

**Use when:**
- refining workflows
- improving performance
- simplifying structure

---

### 5. CREATION

**Purpose:**  
Build new components.

**Behavior:**
- structured output
- aligned with system laws
- no uncontrolled expansion
- clarity over creativity

**Use when:**
- generating new files
- defining systems
- writing structured content

---

### 6. REVIEW

**Purpose:**  
Validate completed work.

**Behavior:**
- strict checking
- comparison against rules
- identify deviations
- no new creation

**Use when:**
- before marking COMPLETE
- validating outputs
- ensuring alignment

---

### 7. RECOVERY

**Purpose:**  
Handle errors and failures.

**Behavior:**
- isolate issue
- prevent further damage
- prepare correction path
- minimal action only

**Use when:**
- FAILED state
- system instability
- corrupted outputs

---

### 8. AUDIT

**Purpose:**  
System-level verification.

**Behavior:**
- check logs
- verify consistency
- ensure rule compliance
- no modification unless required

**Use when:**
- reviewing history
- validating system integrity
- compliance checks

---

## III. MODE RULES

### RULE 1 — ONE MODE ONLY
Agent must operate under a single mode at a time.

---

### RULE 2 — MODE MUST MATCH STATE

Examples:

- IDLE → SAFE
- READY → ANALYSIS / SAFE
- ACTIVE → EXECUTION / CREATION / OPTIMIZATION
- REVIEW → REVIEW / ANALYSIS
- FAILED → RECOVERY
- BLOCKED → SAFE
- COMPLETE → SAFE

---

### RULE 3 — NO MODE WITHOUT PURPOSE

Mode must be explicitly justified by:
- task type
- system condition
- execution phase

---

### RULE 4 — NO MIXED BEHAVIOR

Agent must not:
- analyze while executing
- create while reviewing
- optimize without scope

---

### RULE 5 — SAFE FALLBACK

If mode is unclear:

MODE: SAFE

---

## IV. MODE TRANSITIONS

Allowed transitions:

- SAFE → ANALYSIS
- ANALYSIS → EXECUTION
- EXECUTION → REVIEW
- REVIEW → COMPLETE
- EXECUTION → OPTIMIZATION
- FAILED → RECOVERY
- RECOVERY → READY

Forbidden:

- EXECUTION → CREATION (without task scope)
- REVIEW → EXECUTION (without reset)
- SAFE → EXECUTION (without READY)

---

## V. MODE LOG FORMAT

MODE must be trackable.

Minimum format:

AGENT: [name]  
STATE: [current state]  
MODE: [current mode]  
TIMESTAMP: [YYYY-MM-DD HH:MM UTC]  
REASON: [why this mode is active]

---

## VI. FAILURE CONTROL

If incorrect mode is detected:

Agent must:
1. stop
2. switch to SAFE
3. report inconsistency
4. await correction

---

## VII. SYSTEM INTEGRITY PRINCIPLE

STATE without MODE = uncontrolled execution  
MODE without STATE = undefined behavior

Both must always exist together.

---

## VIII. FINAL STANDARD

Correct system behavior requires:

- clear state
- correct mode
- valid transition

If MODE is wrong:
→ output becomes inconsistent

If MODE is missing:
→ system becomes unpredictable

Therefore:

MODE defines execution quality.
