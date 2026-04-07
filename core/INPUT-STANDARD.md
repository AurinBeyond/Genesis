# INPUT STANDARD v2.0
# AurinBeyond / Genesis — Execution Layer
# Status: ACTIVE

---

## 1. PURPOSE

This document defines the required structure for all task input in the GENESIS system.

**Why input standardization is necessary:**
- Agents cannot guess user intent. They require explicit, structured instructions.
- Free-form tasks create routing ambiguity, which produces wrong agent activation and degraded output.
- Structured input makes every task checkable, routable, and auditable before a single agent runs.

**Problems it prevents:**
- Agents acting on vague or incomplete instructions
- Output produced without a defined goal or scope
- Routing errors from undefined task type
- Silent failure caused by missing constraints

**How it improves execution:**
- The runtime can route without interpretation
- Validation can reject bad input before any cost is incurred
- Every task is traceable from intake to completion

**Why free-form tasks create instability:**
A free-form task forces every agent to make assumptions. Those assumptions compound. The output drifts from the original intent. The system cannot log what it did not know.

**No structured input = no execution.**

---

## 2. INPUT ENTRY RULE

Every task must enter the system through a structured format. The system must flag or reject tasks that are:

- vague (no clear goal or output defined)
- incomplete (missing one or more mandatory fields)
- contradictory (constraints conflict with requested output)
- unroutable (task type does not match any registered type)

Tasks that fail this rule are written to `logs/failures.log` and do not proceed.

---

## 3. MANDATORY INPUT FIELDS

Every valid task must contain the following fields. There are no exceptions.

| Field | Required | Description |
|---|---|---|
| Task Title | Yes | Clear, human-readable name for the task |
| Task Type | Yes | Classification from the registered type list |
| Objective | Yes | What this task must achieve |
| Context | Yes | Background information, existing assets, current state |
| Constraints | Yes | Scope limits, brand rules, format rules |
| Requested Output | Yes | Exact format and location of the expected output |
| Priority | Yes | Execution urgency level |
| Language | Yes | Language(s) for output |
| Target Agent | No | Override agent selection if needed |
| Status | Yes | Current state of the task at intake |

---

## 4. FIELD DEFINITIONS

### Task Title

**What it means:** A short, clear name for the task. Used in logs, PR titles, and tracking.

**Why it matters:** Without a title, the task cannot be referenced in logs or tracked across runs.

**Valid:** `Create Gumroad sales page for first offer`

**Invalid:** `do the page thing` / `(blank)`

---

### Task Type

**What it means:** The classification that determines which agents execute and in what order.

**Why it matters:** Routing depends entirely on task type. An unrecognized type blocks execution.

**Valid:** `page-structure`

**Invalid:** `I need some content` / `misc`

---

### Objective

**What it means:** A single, unambiguous statement of what this task must produce.

**Why it matters:** The objective is the reference point for validation. If output does not achieve the objective, it fails.

**Valid:** `Produce complete sales page copy for the first Gumroad product`

**Invalid:** `make it better` / `do something with this`

---

### Context

**What it means:** Background that the agent needs to execute the task correctly.

**Why it matters:** Without context, agents produce generic output that does not fit the system's existing state.

**Valid:** `This is the first paid product in the AurinBeyond pipeline. The offer has been approved in TASK-001. Existing brand tone rules apply.`

**Invalid:** `you know what this is` / `(blank)`

---

### Constraints

**What it means:** A list of rules the output must respect. Must be actionable, not emotional.

**Why it matters:** Constraints prevent output drift. They are checked during validation.

**Valid:** `no hype language`, `max 800 words`, `preserve existing section structure`, `no unverified statistics`

**Invalid:** `make it feel right` / `don't make it weird`

---

### Requested Output

**What it means:** The exact format, file, or artifact that must exist when the task is complete.

**Why it matters:** If output type is undefined, agents cannot produce the correct artifact.

**Valid:** `Create logs/outputs/TASK-002/FINAL.md containing the full sales page copy`

**Invalid:** `write the stuff` / `improve it`

---

### Priority

**What it means:** The urgency level that determines scheduling and review order.

**Why it matters:** Prevents all tasks being treated equally. Prevents misuse of CRITICAL status.

**Valid:** `HIGH`

**Invalid:** `urgent!!!` / `as soon as possible`

---

### Language

**What it means:** The language(s) in which the output must be produced.

**Why it matters:** No agent may assume language. Multilingual outputs require explicit declaration.

**Valid:** `English`, `English (source) + Estonian (output)`, `English only`

**Invalid:** `(blank)` / `whatever works`

---

### Target Agent

**What it means:** An optional override to specify which agent(s) should handle this task.

**Why it matters:** Normally the runtime determines routing from task type. This field is only used when a specific agent must be forced.

**Valid:** `Brand Guardian`, `(blank — runtime decides)`

**Invalid:** `all agents` / `whoever can do it`

---

### Status

**What it means:** The intake state of the task.

**Why it matters:** The runtime reads this field to determine whether to execute, hold, or skip.

**Valid:** `NEW`, `READY FOR ROUTING`, `BLOCKED`, `INCOMPLETE`

**Invalid:** `done soon` / `in progress maybe`

---

## 5. TASK TYPE CLASSIFICATION

The `Task Type` field determines which agents are activated. Only registered types are valid.

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
| `translation` | Adapt content to another language | Language Polisher |
| `content-audit` | Review existing content for quality | Brand Guardian + Semantic Core |

Tasks with unregistered types are flagged as `INVALID` and execution is blocked.

---

## 6. PRIORITY SYSTEM

| Level | Meaning | When to use |
|---|---|---|
| `LOW` | Can be deferred without impact | Cleanup tasks, non-blocking improvements |
| `NORMAL` | Standard execution order | Default for most tasks |
| `HIGH` | Prioritized over NORMAL tasks | Time-sensitive output, dependent tasks blocked |
| `CRITICAL` | Immediate execution required | System integrity failures, blocking all other work |

**CRITICAL misuse rule:** `CRITICAL` must not be used for convenience or impatience. A task is CRITICAL only when the system cannot progress in any direction without it. Repeated misuse invalidates the priority system.

---

## 7. LANGUAGE FIELD RULES

The Language field must declare one of the following:

| Declaration | Meaning |
|---|---|
| `English` | Output is in English only |
| `Estonian` | Output is in Estonian only |
| `English + Estonian` | Both languages required in output |
| `[source language] → [output language]` | Translation or adaptation task |

No agent may guess the language. If the field is blank, execution is blocked.

---

## 8. CONSTRAINTS FIELD RULES

Constraints must be:

- **Actionable** — an agent can apply them during execution
- **Specific** — not emotional or vague
- **Non-contradictory** — they do not conflict with the requested output

**Valid constraint examples:**
- `no hype language`
- `legal-safe wording only`
- `output must be under 600 words`
- `preserve existing section headings`
- `avoid duplication with TASK-001 output`
- `use only approved brand terminology`

**Invalid constraint examples:**
- `make it feel authentic` — not actionable
- `don't make it bad` — not specific
- `no limits` — contradicts the purpose of constraints

---

## 9. REQUESTED OUTPUT RULES

The Requested Output field must specify:

- The output format (file, list, template, structured text)
- The output location (file path if applicable)
- Whether it replaces or supplements existing content

**Valid examples:**
- `Create logs/outputs/TASK-003/FINAL.md containing the full funnel copy`
- `Revise core/TASK.md to include the updated context section`
- `Generate a structured response template at logs/outputs/TASK-004/chat-template.md`

**Invalid examples:**
- `make it better` — no format or location
- `improve everything` — scope undefined
- `do something smart` — not actionable

---

## 10. STATUS MODEL

Tasks enter with one of the following statuses:

| Status | Meaning | Runtime action |
|---|---|---|
| `NEW` | Task created, not yet validated | Runtime checks and routes |
| `READY FOR ROUTING` | Validated, awaiting agent selection | Runtime activates agents |
| `BLOCKED` | Execution cannot proceed — dependency missing | Runtime logs and halts |
| `INCOMPLETE` | Task line exists but required fields are missing | Runtime logs and flags |

The runtime reads status at intake. If status is `BLOCKED` or `INCOMPLETE`, no execution begins.

---

## 11. INPUT VALIDATION RULES

Input is **VALID** only if ALL of the following conditions are true:

| Condition | Required |
|---|---|
| Task Title is present and non-empty | Yes |
| Task Type is registered | Yes |
| Objective is specific and actionable | Yes |
| Context provides sufficient background | Yes |
| Constraints are actionable | Yes |
| Requested Output is defined with format and location | Yes |
| Priority is one of: LOW, NORMAL, HIGH, CRITICAL | Yes |
| Language is declared | Yes |
| Status is one of the valid intake states | Yes |

If any condition fails, the task is flagged and logged. Execution does not begin.

---

## 12. REJECTION CONDITIONS

The system must reject or hold any task that is:

| Condition | Result |
|---|---|
| Objective is vague or missing | Flagged INCOMPLETE |
| Requested output is undefined | Flagged INCOMPLETE |
| Task type is unregistered | Flagged INVALID |
| Constraints conflict with objective | Flagged BLOCKED |
| Duplicate of an existing active task | Flagged BLOCKED |
| Required fields are blank | Flagged INCOMPLETE |
| Language field is empty | Flagged INCOMPLETE |

All rejections are logged in `logs/failures.log` before any agent runs.

---

## 13. CANONICAL INPUT TEMPLATE

All tasks must follow this template. Use `core/TASK.md` for extended context.

```
Task Title:       [Clear, human-readable task name]
Task Type:        [Registered type from Section 5]
Objective:        [What this task must produce — one clear statement]
Context:          [Background, existing state, relevant prior tasks]
Constraints:      [Actionable rules — no hype, max length, format rules, etc.]
Requested Output: [Exact format and file path of expected output]
Priority:         [LOW | NORMAL | HIGH | CRITICAL]
Language:         [English | Estonian | English + Estonian | source → output]
Target Agent:     [Optional — leave blank for runtime to decide]
Status:           [NEW | READY FOR ROUTING | BLOCKED | INCOMPLETE]
```

---

## 14. EXAMPLES

### Valid Example

```
Task Title:       Create sales page copy for first Gumroad product
Task Type:        page-structure
Objective:        Produce complete sales page copy for the AurinBeyond first offer
Context:          Offer defined in TASK-001 output. Brand rules in core/GENESIS-LAWS.md apply.
                  Audience: adults 25-45 questioning their identity and decision patterns.
Constraints:      no hype language, no false urgency, max 900 words, no unverified claims
Requested Output: logs/outputs/TASK-002/FINAL.md — full sales page copy, structured with sections
Priority:         HIGH
Language:         English
Target Agent:     (blank — runtime decides)
Status:           NEW
```

**Why it passes:** All required fields are present. Objective is specific. Output has a defined path. Constraints are actionable. Type is registered.

---

### Incomplete Example

```
Task Title:       Write the about page
Task Type:        page-structure
Objective:        (blank)
Context:          (blank)
Constraints:      make it good
Requested Output: (blank)
Priority:         HIGH
Language:         (blank)
Target Agent:     (blank)
Status:           INCOMPLETE
```

**Why it fails:** Objective is missing. Context is missing. Requested Output is missing. Language is blank. Constraint is not actionable. Runtime blocks execution and logs to `failures.log`.

---

### Invalid Example

```
Task Title:       Improve everything
Task Type:        content-magic
Objective:        make the whole system better
Context:          you know what needs doing
Constraints:      no limits
Requested Output: improve it
Priority:         CRITICAL
Language:         whatever
Status:           (blank)
```

**Why it fails:** Task type `content-magic` is not registered. Objective is vague. Constraints are contradictory. Requested output is not actionable. Language is not declared. Priority CRITICAL is misused. Runtime blocks execution and logs to `failures.log`.

---

## 15. INPUT REJECTION PROTOCOL

When input is rejected:

1. `logs/failures.log` receives a structured entry:
   ```
   [YYYY-MM-DD HH:MM] TASK-ID → failure: input rejected — reason: [reason] — state: BLOCKED (GENESIS-RUNTIME)
   ```

2. The GitHub Actions run exits as failed.

3. No partial output is written.

4. Source is notified via the failed run status in GitHub Actions.

5. To resume, correct the input in `TASKMASTER.md` or `core/TASK.md` and re-trigger the workflow.

---

## 16. INPUT IMMUTABILITY RULE

Once a task has been executed and marked complete (`[x]`):
- Its entry in `TASKMASTER.md` must not be edited or reverted
- New tasks must be added as new entries
- Completed tasks serve as the audit history of the system

---

**This standard is version-locked. Changes require a version bump in the file header.**
