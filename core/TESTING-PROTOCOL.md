# TESTING PROTOCOL v1.0

## CORE PRINCIPLE

> A system is not stable because it looks correct.
> It is stable only if it survives realistic use without confusion, drift, duplication, or hidden failure.

---

## 1. PURPOSE

Testing is not a final check before launch. It is a structured verification that the system behaves as designed under conditions that reflect real use.

**Why testing is necessary:**
- Architecture defines intent. Testing confirms whether execution matches that intent.
- GENESIS operates through agent cooperation. Each agent depends on clean input from the layer before it. A failure at any layer propagates downstream unless caught.
- Outputs that pass internally but fail in human context cannot be detected by logic alone — they require deliberate scenario-based verification.

**What kinds of failure it prevents:**
- Incorrect agent routing (wrong agent receives a task).
- Silent validation failure (output passes internal checks but is actually weak or non-compliant).
- Execution drift (system gradually deviates from intended behavior across repeated runs).
- Agent conflict (two agents produce contradictory outputs that merge without resolution).
- Bloat accumulation (outputs grow in length and noise without delivering more value).
- Invisible failure (an agent fails and the system continues as if it did not).

**Why architecture alone is not proof of readiness:**
- A well-designed system can still fail at runtime due to edge cases, ambiguous inputs, or unexpected agent interaction.
- Documentation describes desired behavior. Tests verify actual behavior.
- Without tests, "stability" is assumption — not evidence.

**How testing protects long-term system stability:**
- Establishes a verified baseline before deployment.
- Makes regressions detectable when the system changes.
- Enables controlled updates by isolating which layers are affected by a change.
- Prevents gradual drift from becoming permanent system degradation.

---

## 2. TESTING SCOPE

The following areas must be covered in every full test cycle. No area may be skipped if it is relevant to a system change.

| Area                   | What is Verified                                                       |
|------------------------|------------------------------------------------------------------------|
| Input Acceptance       | Structured, incomplete, contradictory, and vague inputs are handled correctly |
| Routing Accuracy       | Tasks reach the correct agent(s) and only the correct agent(s)          |
| Execution Order        | Agents execute in the correct sequence; no upstream step is skipped     |
| Output Validation      | Output meets structural, tonal, and content standards before delivery   |
| Logging Behavior       | All critical moments are logged; no silent execution occurs             |
| Failure Handling       | Failures are caught, logged, and escalated; not silently passed through |
| Agent Non-Conflict     | Agents do not overwrite or contradict each other's valid outputs        |
| Duplication Prevention | Identical or near-identical tasks do not produce duplicate outputs      |
| Noise Control          | Outputs do not contain filler, padding, or content without clear purpose |
| Human Coherence        | Outputs are readable, natural, and appropriate for the intended audience |

---

## 3. TEST TYPES

### A. Input Tests

Verify the system's ability to correctly process or reject inputs.

| Sub-type           | Test Condition                                                             | Expected Behavior                          |
|--------------------|----------------------------------------------------------------------------|---------------------------------------------|
| Valid structured   | Input meets all required fields and format                                | Accepted; routing begins                    |
| Incomplete input   | One or more required fields are missing                                   | Rejected; failure logged; reason returned   |
| Contradictory input| Input contains conflicting requirements (e.g., brief AND exhaustive)      | Flagged for review; not silently resolved   |
| Vague input        | Input lacks sufficient detail to determine agent or task type             | Returned for clarification; not guessed     |

---

### B. Routing Tests

Verify that task routing selects the correct agents and excludes irrelevant ones.

| Sub-type                  | Test Condition                                              | Expected Behavior                              |
|---------------------------|-------------------------------------------------------------|------------------------------------------------|
| Correct agent selection   | Task type clearly maps to one or more agents                | Correct agents selected; none missing          |
| No unnecessary agents     | Task type does not require all agents                       | Only required agents are invoked               |
| Context-sensitive routing | Same task type with different context may route differently | Routing reflects context, not just task label  |

---

### C. Execution Flow Tests

Verify that agents execute in the correct order without skipping, looping, or stalling.

| Sub-type                   | Test Condition                                              | Expected Behavior                                   |
|----------------------------|-------------------------------------------------------------|-----------------------------------------------------|
| Correct sequence           | Multi-agent task with defined execution order               | Each agent executes after its upstream dependency   |
| No skipped layers          | Validation layer is required before output delivery         | Validation cannot be bypassed                       |
| No execution loop          | Task triggers the same agent repeatedly                     | Loop is detected and blocked after one retry        |
| No stall                   | Agent receives valid input but does not produce output      | Stall is detected; failure logged; execution halted |

---

### D. Validation Tests

Verify the output validation layer correctly distinguishes valid, weak, and invalid outputs.

| Sub-type             | Test Condition                                              | Expected Behavior                        |
|----------------------|-------------------------------------------------------------|------------------------------------------|
| Incomplete output    | Output is missing a required structural section             | FAIL; rewrite triggered                  |
| Weak output          | Output is technically complete but tone or clarity is poor  | WARNING; flagged for review              |
| Valid output         | Output meets all structural and content standards           | PASS; ready for delivery                 |

---

### E. Logging Tests

Verify that logs are produced at all mandatory moments as defined in `LOGGING-STANDARD.md`.

| Sub-type               | Test Condition                                              | Expected Behavior                                    |
|------------------------|-------------------------------------------------------------|------------------------------------------------------|
| Input acceptance       | Input is accepted or rejected                               | Entry written to `updates.log` or `failures.log`     |
| Routing decision       | Agent routing occurs                                        | Entry written to `decisions.log`                     |
| Execution completion   | Agent completes its task                                    | Entry written to `updates.log`                       |
| Validation failure     | Output fails validation                                     | Entry written to `failures.log` with RETRY flag      |
| Silent failure check   | Agent fails without logging                                 | Test fails — no silent execution is permitted        |

---

### F. Hygiene Tests

Verify that the system does not accumulate unnecessary files, outputs, or content.

| Sub-type                  | Test Condition                                              | Expected Behavior                              |
|---------------------------|-------------------------------------------------------------|------------------------------------------------|
| Duplicate file prevention | Same task submitted twice                                   | Second execution is flagged; no duplicate file |
| Expansion control         | Agent adds sections not requested in input                  | Extra content is flagged as out-of-scope       |
| Output conciseness        | Output exceeds defined length without added value           | Flagged as bloat; trimming triggered           |

---

### G. Human Coherence Tests

Verify that outputs meet human readability and naturalness standards.

| Sub-type              | Test Condition                                              | Expected Behavior                                      |
|-----------------------|-------------------------------------------------------------|--------------------------------------------------------|
| Non-robotic tone      | Output reads as generated by a machine                      | Flagged; Language Polisher layer activated             |
| Natural tone          | Output reads naturally and appropriately for the audience   | PASS                                                   |
| Guidance clarity      | Instructions or guidance are unclear or require inference   | Flagged; clarity rewrite triggered                     |

---

## 4. TEST SCENARIO DESIGN

Each test scenario must be constructed before execution using the following structure. No freeform testing is permitted.

```
SCENARIO TITLE:    [Short descriptive name]
TASK TYPE:         [content / routing / hygiene / validation / etc.]
INPUT STRUCTURE:   [Summary of input fields and values provided]
EXPECTED ROUTING:  [Which agents should be selected and in what order]
EXPECTED OUTPUT:   [Description of the correct output state]
EXPECTED LOGS:     [Which logs should contain entries, and of what type]
EXPECTED RESULT:   [PASS / PASS WITH WARNING / FAIL]
```

Scenarios must reflect realistic task requests — not theoretical edge cases invented to fill a quota. Every scenario must be derived from a plausible real-world usage pattern.

---

## 5. MINIMUM REQUIRED TEST SCENARIOS

The following scenarios must be present in every test cycle. Additional scenarios may be added but these ten are mandatory.

---

**SCENARIO 01 — Clear Valid Task**
```
SCENARIO TITLE:    Clear valid task execution
TASK TYPE:         Content generation — long-form insight
INPUT STRUCTURE:   Topic, audience, tone, length, language — all fields complete and consistent
EXPECTED ROUTING:  Semantic Core → Brand Intelligence → ContentAgent → Language Polisher → Validation
EXPECTED OUTPUT:   Complete structured output; all modules present; tone compliant
EXPECTED LOGS:     updates.log (accepted, start, complete); decisions.log (routing); updates.log (validation pass)
EXPECTED RESULT:   PASS
```

---

**SCENARIO 02 — Incomplete Task**
```
SCENARIO TITLE:    Task missing required input field
TASK TYPE:         Content generation — short-form
INPUT STRUCTURE:   Topic and tone provided; audience and language missing
EXPECTED ROUTING:  Input layer only — task does not proceed to agents
EXPECTED OUTPUT:   No output generated; clarification request returned
EXPECTED LOGS:     failures.log (input rejected, missing fields, RETRY: YES)
EXPECTED RESULT:   FAIL
```

---

**SCENARIO 03 — Duplicated Task Request**
```
SCENARIO TITLE:    Identical task submitted twice in sequence
TASK TYPE:         Content generation — repeated request
INPUT STRUCTURE:   Same input submitted again within the same session or without state reset
EXPECTED ROUTING:  Hygiene check intercepts before routing; second task blocked
EXPECTED OUTPUT:   No duplicate output; existing output referenced
EXPECTED LOGS:     decisions.log (duplicate detected, blocked); updates.log (reference to original execution)
EXPECTED RESULT:   PASS WITH WARNING
```

---

**SCENARIO 04 — Multilingual Task**
```
SCENARIO TITLE:    Task requested in non-default language
TASK TYPE:         Content generation — language-specific output
INPUT STRUCTURE:   All required fields complete; language declared as Estonian
EXPECTED ROUTING:  Semantic Core → Brand Intelligence → ContentAgent → Language Polisher (language-aware)
EXPECTED OUTPUT:   Output in Estonian; tone and cultural alignment verified
EXPECTED LOGS:     decisions.log (language flag noted); updates.log (completion); validation log entry
EXPECTED RESULT:   PASS
```

---

**SCENARIO 05 — High-Risk Task Requiring Review**
```
SCENARIO TITLE:    Task with sensitive or high-impact content request
TASK TYPE:         Content generation — topic adjacent to healing or diagnosis claims
INPUT STRUCTURE:   Topic touching on mental health patterns; all fields complete
EXPECTED ROUTING:  Semantic Core → Brand Intelligence (flags for review) → HOLD
EXPECTED OUTPUT:   No output delivered; READY WITH REVIEW state returned
EXPECTED LOGS:     decisions.log (review flag, reason stated); failures.log if blocked
EXPECTED RESULT:   PASS WITH WARNING
```

---

**SCENARIO 06 — Unclear Routing Case**
```
SCENARIO TITLE:    Task type does not map cleanly to a single agent
TASK TYPE:         Ambiguous — could be insight or instruction
INPUT STRUCTURE:   Topic provided; output type not specified; tone neutral
EXPECTED ROUTING:  Orchestrator requests clarification; routing deferred
EXPECTED OUTPUT:   No output; clarification required
EXPECTED LOGS:     decisions.log (routing deferred, reason: ambiguous task type); failures.log not triggered
EXPECTED RESULT:   PASS WITH WARNING
```

---

**SCENARIO 07 — Task That Should Be Blocked**
```
SCENARIO TITLE:    Task requesting content violating GENESIS-LAWS
TASK TYPE:         Content generation — prohibited claim type
INPUT STRUCTURE:   Task explicitly requests healing or therapeutic outcome language
EXPECTED ROUTING:  Brand Intelligence blocks immediately; task does not reach ContentAgent
EXPECTED OUTPUT:   BLOCKED state; reason returned
EXPECTED LOGS:     failures.log (blocked, reason: GENESIS-LAWS violation, RETRY: NO)
EXPECTED RESULT:   FAIL
```

---

**SCENARIO 08 — Task That Should Pass With Review**
```
SCENARIO TITLE:    Task with borderline tone — requires human confirmation
TASK TYPE:         Content generation — tone near boundary of allowed language
INPUT STRUCTURE:   All fields complete; topic is emotionally weighted but not prohibited
EXPECTED ROUTING:  Full agent chain executes; output produced but held at delivery
EXPECTED OUTPUT:   Output generated; status = READY WITH REVIEW
EXPECTED LOGS:     updates.log (execution complete); decisions.log (review required, tone flagged)
EXPECTED RESULT:   PASS WITH WARNING
```

---

**SCENARIO 09 — Task That Should Fail Validation**
```
SCENARIO TITLE:    Output fails validation on first pass
TASK TYPE:         Content generation — output produced but non-compliant
INPUT STRUCTURE:   Valid input; agent produces output missing MODULE 3
EXPECTED ROUTING:  Full chain; ValidationAgent rejects output; rewrite triggered
EXPECTED OUTPUT:   No final output; rewrite initiated
EXPECTED LOGS:     failures.log (validation fail, incomplete structure, RETRY: YES); updates.log (rewrite started)
EXPECTED RESULT:   FAIL
```

---

**SCENARIO 10 — Task Risking Noise or Bloat**
```
SCENARIO TITLE:    Output produced with excessive length and padding
TASK TYPE:         Content generation — long-form with padding risk
INPUT STRUCTURE:   Valid input; agent generates output 40% longer than required with filler content
EXPECTED ROUTING:  Validation layer detects bloat; Language Polisher activated for trim
EXPECTED OUTPUT:   Trimmed output returned; bloat sections removed
EXPECTED LOGS:     decisions.log (bloat detected, polisher triggered); updates.log (revised output complete)
EXPECTED RESULT:   PASS WITH WARNING
```

---

## 6. PASS / FAIL RULES

### PASS

**Conditions:**
- All expected routing occurred and nothing unexpected was triggered.
- Output meets all structural, tonal, and content requirements.
- All mandatory log entries are present and correctly formatted.
- No agent conflict or duplication was detected.

**Action after PASS:** Task execution confirmed stable. Log result in test report. No system change required.

---

### PASS WITH WARNING

**Conditions:**
- Core execution succeeded but one or more secondary issues were detected: borderline tone, routing ambiguity, minor hygiene flag, or deferred review.
- Output was produced but requires human review before live delivery.
- A non-critical log entry was missing or imprecise.

**Action after PASS WITH WARNING:** Document the warning. Determine whether a system rule needs clarification. If the same warning recurs across multiple tests, treat as a latent defect.

---

### FAIL

**Conditions:**
- Routing was incorrect, missing, or triggered an unintended agent.
- Output did not meet validation requirements and was not corrected.
- A mandatory log entry is absent.
- A failure occurred silently (no log, no block, no flag).
- A prohibited output type was produced (e.g., healing claim, bloat, duplicate).

**Action after FAIL:** Execution must stop. Failure is logged. Affected layer is identified. System must not be considered stable or deployed until the failure is resolved and retested.

---

## 7. SYSTEM STABILITY CHECKS

These tests verify system resilience under pressure — not just single-task correctness.

| Check                               | Method                                                                 | Pass Condition                                               |
|-------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| Repeated task handling              | Submit the same valid task five times in sequence                      | Consistent output quality; no degradation or drift           |
| Similar task collision              | Submit two near-identical tasks simultaneously                         | Both handled independently; no output merging                |
| Overlapping agent scope             | Submit a task that two agents could both claim                         | Routing resolves cleanly; one agent handles; no conflict     |
| Incomplete upstream input           | Agent receives output from a prior agent that is missing required data | Agent flags missing input; does not guess or fabricate       |
| Failure recovery behavior           | First agent in a chain fails                                           | Downstream agents do not execute; failure logged; chain halts |

---

## 8. NON-BLOCKING & RECOVERY TESTS

Define the system's behavior when one component fails while others remain valid.

| Test                                | Scenario                                                               | Expected Behavior                                             |
|-------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------|
| Isolated agent failure              | Language Polisher fails; all other agents succeeded                    | Failure logged; partial execution visible; output held        |
| Partial execution visibility        | Chain halts mid-execution                                              | All completed steps logged; failure point identified in log   |
| Safe blocking                       | ValidationAgent blocks output                                          | Output not delivered; task status set to BLOCKED              |
| Retry pathway                       | Validation failure with `RETRY: YES` flag                             | Rewrite triggered automatically or flagged for manual retry   |
| No hidden failure                   | Any agent in the chain encounters an error                             | Error must appear in `failures.log`; no silent continuation   |

---

## 9. EDGE CASE TESTS

| Edge Case                                 | Test Condition                                                            | Expected Behavior                                              |
|-------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------|
| Contradictory constraints                 | Input requires output to be both very brief and exhaustively detailed     | Flagged as contradictory; returned for clarification           |
| Impossible requested output               | Input requests something outside GENESIS capability or legal scope        | BLOCKED; reason logged; no partial attempt produced            |
| Excessive task complexity                 | Input contains 10+ distinct requirements within one task                  | Decomposition required; task returned for scoping              |
| Wrong language declaration                | Input declares Estonian; topic and tone are mismatched for that language   | Language Polisher flags mismatch; human review triggered       |
| Technically correct but humanly poor      | Output passes all structural checks but reads as robotic and hollow        | Validation flags coherence failure; Language Polisher activated |

---

## 10. HUMAN REVIEW TESTS

These tests verify that the system's three review states — READY, READY WITH REVIEW, and BLOCKED — are produced correctly and are not interchangeable.

| State               | Trigger Condition                                                                     | Must NOT Appear When                                               |
|---------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| READY               | All validations pass; no flags; output meets all standards                            | Any flag, warning, or unresolved issue is present                  |
| READY WITH REVIEW   | Output passes structure and safety; borderline tone, sensitivity, or ambiguity noted  | Task was blocked; validation failed critically                     |
| BLOCKED             | Output violates GENESIS-LAWS; input was prohibited; failure cannot be retried          | Output is simply weak — weakness alone does not block              |

**Test for each state:**
- READY: Submit a clean, well-formed task. Verify state = READY and no review flag exists.
- READY WITH REVIEW: Submit a task with borderline content. Verify state = READY WITH REVIEW and review reason is logged.
- BLOCKED: Submit a task requesting prohibited output. Verify state = BLOCKED and `failures.log` contains the reason with `RETRY: NO`.

---

## 11. TEST REPORT FORMAT

Every executed test must produce a report using this exact structure:

```
TEST ID:          [T-NNN]
SCENARIO NAME:    [Scenario title from Section 5 or custom scenario name]
INPUT SUMMARY:    [One sentence describing the input provided]
EXPECTED RESULT:  [PASS / PASS WITH WARNING / FAIL]
ACTUAL RESULT:    [PASS / PASS WITH WARNING / FAIL]
LOGS CHECKED:     [List of logs reviewed: updates.log, decisions.log, failures.log]
STATUS:           [CONFIRMED / DISCREPANCY / ESCALATED]
NOTES:            [One sentence. If discrepancy, describe it. If PASS, state "No issues found."]
```

**STATUS definitions:**
- `CONFIRMED` — actual result matches expected result.
- `DISCREPANCY` — actual result differs from expected result; investigation required.
- `ESCALATED` — discrepancy indicates a system-level defect; deployment must be held.

---

## 12. TEST EXECUTION FREQUENCY

Tests must be run at the following points. All are mandatory.

| Trigger                                        | Required Scope                                            |
|------------------------------------------------|-----------------------------------------------------------|
| Before live deployment                         | Full test cycle — all 10 mandatory scenarios + stability  |
| After major runtime changes                    | Full test cycle                                           |
| After orchestration changes                    | Routing tests + execution flow tests + logging tests      |
| After validation logic changes                 | Validation tests + output tests + logging tests           |
| After adding a new agent or major layer        | Full test cycle                                           |
| After repeated identical failures in live use  | Targeted tests on affected layer + failure recovery tests |

Ad-hoc testing is permitted but does not replace scheduled cycles.

---

## 13. FAILURE ESCALATION RULE

When one or more tests produce a FAIL result:

1. **System is not stable.** No deployment or live execution proceeds until failures are resolved.
2. **Failure is logged** in `failures.log` with the test ID, affected layer, and reason.
3. **Affected layer is identified.** The failure is not treated as isolated unless evidence confirms it is.
4. **Fix is implemented** and the specific failing test is re-executed to confirm resolution.
5. **If the failure is systemic** (same layer failing across multiple scenarios), a full test cycle is re-run after the fix.
6. **Release or live execution is blocked** for as long as any unresolved FAIL state exists in the current cycle.

No known failure may be deferred to post-deployment.

---

## 14. NON-BLOAT TESTING RULE

The test suite itself must remain clean and purposeful.

- Do not create tests that duplicate an existing scenario with only cosmetic differences.
- Do not add tests to increase test count without adding coverage of a new failure mode.
- Each test must protect against a specific, realistic failure that is not already covered.
- Test reports must be concise. One-line notes. No narrative padding.
- Review the test suite when adding new scenarios to confirm no redundancy is introduced.

---

## 15. EXAMPLES

### PASS Example

```
TEST ID:          T-001
SCENARIO NAME:    Clear valid task execution
INPUT SUMMARY:    Long-form insight task; all fields complete; language Estonian; topic: pattern recognition.
EXPECTED RESULT:  PASS
ACTUAL RESULT:    PASS
LOGS CHECKED:     updates.log, decisions.log
STATUS:           CONFIRMED
NOTES:            No issues found. All modules present; tone compliant; routing correct.
```

**Why PASS:** All routing occurred as expected, output passed validation on first pass, all mandatory log entries were present, and no flags were triggered.

---

### PASS WITH WARNING Example

```
TEST ID:          T-008
SCENARIO NAME:    Task with borderline tone — requires human confirmation
INPUT SUMMARY:    Content task on emotionally weighted topic; all fields complete; tone near boundary.
EXPECTED RESULT:  PASS WITH WARNING
ACTUAL RESULT:    PASS WITH WARNING
LOGS CHECKED:     updates.log, decisions.log
STATUS:           CONFIRMED
NOTES:            Tone flag raised by Brand Intelligence; output held at READY WITH REVIEW; human approval required before delivery.
```

**Why PASS WITH WARNING:** Execution completed and output was produced, but a non-critical flag required human review before delivery. The warning is expected and correctly handled.

---

### FAIL Example

```
TEST ID:          T-007
SCENARIO NAME:    Task requesting content violating GENESIS-LAWS
INPUT SUMMARY:    Request for content describing therapeutic outcomes from product use.
EXPECTED RESULT:  FAIL
ACTUAL RESULT:    FAIL
LOGS CHECKED:     failures.log
STATUS:           CONFIRMED
NOTES:            Task blocked by Brand Intelligence; GENESIS-LAWS violation logged; RETRY: NO; no output produced.
```

**Why FAIL:** The input requested a category of content explicitly prohibited by GENESIS-LAWS. The system correctly blocked the task and produced no output. This is a confirmed FAIL — the task was not completable. The correct system behavior is to block and log, not to attempt a partial output.

---

STATUS: Locked as Baseline // 2026 // GENESIS Runtime
