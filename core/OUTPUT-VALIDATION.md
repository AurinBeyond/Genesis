# OUTPUT VALIDATION v1.0
# AurinBeyond / Genesis — Execution Layer
# Status: ACTIVE

---

## PURPOSE

This document defines the validation rules applied to every agent output before it is accepted as a final result.

Validation runs after agent execution and before the task is marked complete. It is the last gate before output reaches Source review.

**Unvalidated output is not final output.**

---

## I. VALIDATION TRIGGER

Output validation runs:
- After every agent pipeline execution
- Before `TASKMASTER.md` is updated (task is NOT marked complete until validation passes)
- Before output is flagged as `READY`

---

## II. VALIDATION CHECKLIST

Each output file must pass all applicable checks. Checks are marked as PASS, FAIL, or SKIP (if not applicable to output type).

### 1. Structural Completeness

| Check | Rule |
|---|---|
| File exists | Output file is present at the expected path |
| File is non-empty | File contains more than 3 lines |
| Required sections present | Title, intro, and at least one content section are present |
| No placeholder content | No `[INSERT]`, `TBD`, `PLACEHOLDER`, or similar markers remain |
| No truncated output | Content does not end mid-sentence or mid-section |

### 2. Brand Alignment

| Check | Rule |
|---|---|
| Tone is direct and calm | No hype, urgency phrases, or inflated claims |
| No manipulation language | No fear-based phrasing, false scarcity, or pressure tactics |
| No unverified claims | No statistics, percentages, or facts without source basis |
| AurinBeyond voice | Output reflects pattern interruption / conscious choice framing |
| Position accuracy | Describes tools and structure — does not position as therapy or rescue |

### 3. Clarity

| Check | Rule |
|---|---|
| No jargon without definition | Technical or psychological terms are either explained or excluded |
| Sentence complexity | Sentences are clear and direct — no unnecessary complexity |
| Audience alignment | Output is written for the defined reader, not the agent or author |

### 4. No Duplication

| Check | Rule |
|---|---|
| No repeated sections | Same heading or content block does not appear twice |
| No self-referential loops | Output does not describe its own creation process |
| No prior output re-pasted | Output does not contain unmodified blocks from previous task outputs |

### 5. No Excessive Noise

| Check | Rule |
|---|---|
| No meta-commentary | Output does not explain itself or justify its structure |
| No filler phrases | No "In conclusion," "As we can see," or similar |
| No apologies or hedging | Output does not apologize for limitations or hedge claims excessively |
| Length is appropriate | Output is neither padded beyond task scope nor truncated below minimum |

### 6. Correct Routing

| Check | Rule |
|---|---|
| Task type matches content | The content type matches what the task type defined |
| Agent output matches agent role | Offer Architect produces offer content, not funnel content, etc. |
| File is in correct destination | Output is at `logs/outputs/TASK-XXX/[step]-[type].md` |

### 7. Usable Final State

| Check | Rule |
|---|---|
| Output is actionable | Source can take the next defined action without needing to rewrite |
| Output is self-contained | No external references required to understand or use the output |
| Output is review-ready | A human reviewer can evaluate it without needing system context |

---

## III. VALIDATION OUTCOMES

After all checks run, the output receives one of three states:

| State | Condition | Next Action |
|---|---|---|
| `READY` | All checks pass | Task marked complete. Appended to `updates.log`. Source review begins. |
| `READY WITH REVIEW` | Structural checks pass. One or more brand/clarity checks have warnings. | Task flagged. Appended to `updates.log` with `[FLAG]`. Source must review before approval. |
| `BLOCKED` | One or more structural checks fail. | Task NOT marked complete. Appended to `failures.log`. Execution returns to `REVIEW` state. |

---

## IV. FAILURE LOGGING

When validation produces `BLOCKED`:

```
[YYYY-MM-DD HH:MM] TASK-ID → failure: validation failed — checks: [list of failed checks] — state: BLOCKED (GENESIS-RUNTIME)
```

When validation produces `READY WITH REVIEW`:

```
[YYYY-MM-DD HH:MM] TASK-ID → flag: validation passed with warnings — flags: [list of flagged checks] — state: READY WITH REVIEW (GENESIS-RUNTIME)
```

---

## V. VALIDATION SCOPE BY TASK TYPE

Not all checks apply to all task types. The following table defines which check groups apply:

| Task Type | Structural | Brand | Clarity | No Duplication | No Noise | Routing | Usable |
|---|---|---|---|---|---|---|---|
| `offer-creation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `funnel-design` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `raw-copy` | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `voice-refinement` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `brand-validation` | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| `page-structure` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `authority-content` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `legal-compliance` | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ |
| `chat-interaction` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `system-task` | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ |

`raw-copy` and `legal-compliance` skip brand alignment checks — they are refined by downstream agents.

---

## VI. IMMUTABILITY RULE

Validation results are final for each run. They are logged and cannot be edited retroactively. If Source needs to override a `BLOCKED` state, a new task must be created with corrected input.

---

**This standard is locked. Changes require a version bump in the file header.**
