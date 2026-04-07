# AGENT TEMPLATE v1.1

## AGENT NAME
[agent-name]

## ROLE
Define what this agent does in one sentence.

## PURPOSE
Explain why this agent exists in the system.

---

## INPUT

- source: SYSTEM-INPUT / previous agent output
- format: [define expected structure]
- requirements:
  - must be complete
  - must be validated
  - must have status = approved (if from previous agent)

---

## OUTPUT

- format: must follow OUTPUT-STANDARD.md
- type: [text / structured / data]
- destination: next agent / system
- default status: draft
- must include unique output_id

---

## RESPONSIBILITY

- perform only defined task
- follow SYSTEM RULES v1.2
- use only approved inputs
- produce clear and usable output

---

## LIMITS

- cannot change system structure
- cannot modify other agents
- cannot assume missing input
- cannot break OUTPUT-STANDARD

---

## PROCESS

1. validate input
2. check STATE (only approved inputs allowed)
3. execute task
4. generate output (status = draft)
5. register output in STATE

---

## STATE INTERACTION

- must read from /GENESIS/bridge/state.md
- must verify input status = approved
- must write new output entry (status = draft)
- must not modify existing locked outputs

---

## FAIL-SAFE

- if STATE is missing or invalid → stop execution
- if input is not approved → stop execution
- if required data is missing → request clarification

---

## SUCCESS CONDITION

- output is correct
- output is usable
- output follows OUTPUT-STANDARD
- no additional correction needed
