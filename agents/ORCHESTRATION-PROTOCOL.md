# ORCHESTRATION PROTOCOL
# AurinBeyond / Genesis — System Coordination Layer
# Version: 1.0
# Status: ACTIVE

---

## 1. PURPOSE

The Orchestration Protocol exists to ensure the Genesis agent system operates as a single, unified intelligence rather than a collection of independent processes.

**Why it is necessary:**
- Multiple agents operating without coordination produce conflicting, duplicate, or inconsistent outputs.
- Each agent has a defined scope. Without orchestration, agents bleed into each other's responsibilities.
- A shared protocol ensures that every output builds on approved upstream work.

**Problems it prevents:**
- Output conflicts between agents
- Duplication of effort
- Agents acting without required context
- Execution loops or dead ends
- Brand tone inconsistency caused by unsynchronized agents

**How it ensures system stability:**
- All agents follow a fixed execution order.
- No agent acts before its required upstream input is available and approved.
- Failures trigger safe fallback behavior, not system collapse.

**How it enables scalability:**
- New agents can be added to the system without disrupting existing flow, as long as they respect the input/output contract and their assigned step.

---

## 2. AGENT ROLES OVERVIEW

| Agent | Primary Responsibility |
|---|---|
| **System Orchestrator** | Reads the task queue, assigns steps, tracks execution state |
| **Offer Architect** | Defines product identity: name, transformation, format, price, audience |
| **Funnel Architect** | Structures the sales flow: entry, problem, shift, offer, CTA |
| **Content Producer** | Writes raw section copy aligned to approved funnel and page structure |
| **Humanizer** | Transforms raw agent output into brand-consistent, human-voice copy |
| **Brand Guardian** | Validates all outputs against brand identity; assembles the final approved artifact |
| **Genesis Architect** | Defines page structure and section hierarchy — no copy, no code |
| **Frequency Transmitter** | Builds authority content: about, proof, credentials, signal transmission |
| **Semantic Core** | Interprets user intent and semantic meaning from incoming messages |
| **Brand Intelligence** | Applies brand constraints to decisions, classifications, and outputs |
| **Language Polisher** | Refines language quality, removes robotic patterns, adapts register |
| **Chat Agent** | Communicates with users in real time; guides, clarifies, routes |
| **Navigation System** | Determines the correct next step in the user journey |
| **Legal & Compliance Guard** | Produces legal pages and ensures offer compliance |
| **Community Catalyst** | Designs community and contact touchpoints |

---

## 3. EXECUTION FLOW (MANDATORY ORDER)

All agents in an active pipeline must follow this sequence. No step may begin until its upstream dependency is approved.

### Content Pipeline (task-based)

```
1. System Orchestrator     → reads task, assigns first agent
2. Offer Architect         → defines product / offer
3. Funnel Architect        → defines sales flow
4. Content Producer        → writes raw copy
5. Humanizer               → rewrites in human brand voice
6. Brand Guardian          → validates and assembles FINAL output
```

Source approval is required between each step. No agent skips the upstream chain.

### Communication Pipeline (real-time user interaction)

```
1. Semantic Core           → interprets user message and intent
2. Brand Intelligence      → applies brand constraints to the interpretation
3. Chat Agent              → formulates and delivers the response
4. Language Polisher       → refines language quality and register
5. Navigation System       → determines and suggests one next step
```

No agent in this flow may act without the output of the step before it.

### Standalone Tasks

The following agents operate independently when triggered by Source:

- **Genesis Architect** — page structure documents
- **Frequency Transmitter** — authority and trust layer content
- **Legal & Compliance Guard** — legal pages

These agents do not inject into the content pipeline. They run as discrete tasks with their own approval gate.

---

## 4. COLLABORATION RULES

1. **Agents support, not override.** Each agent enhances and advances the work of the previous agent. No agent rewrites completed upstream work without a Source-initiated reset.

2. **Each agent works within its scope.** An agent that writes copy does not define structure. An agent that defines structure does not write copy. Scope is fixed.

3. **No duplication of responsibilities.** If two agents could produce the same output, the task is assigned to one. The other is not triggered.

4. **Structured output passing.** Every agent passes a defined, structured artifact to the next agent. No raw, incomplete, or unformatted data is passed forward.

5. **Read-only access to upstream outputs.** An agent may read any approved upstream artifact but may not modify it. Modification is a Source action.

---

## 5. NON-BLOCKING PRINCIPLE

The system must not stall.

- If an agent encounters ambiguity or incomplete context, it does not halt execution.
- It produces its best output, flags the uncertainty, and passes forward with a `[FLAG: review required]` notation.
- The flag surfaces at the Source approval gate. Source decides whether to proceed or reset.
- An agent may not "freeze" a pipeline step waiting for perfect input. Imperfect input with a flag is valid.

Exception: If an agent determines that proceeding would produce output that violates brand integrity or system rules, it logs the conflict and passes back to Source immediately. It does not guess.

---

## 6. CONFLICT RESOLUTION RULES

When agents produce conflicting outputs or when tone, logic, or brand signals are misaligned:

**Resolution priority:**

1. **Brand Intelligence** — brand identity and constraints take precedence
2. **Semantic Core** — interpreted user intent governs communication logic
3. **System rules** — SYSTEM_RULES.md governs formatting, visual, and structural decisions

**Specific conflict scenarios:**

| Conflict Type | Resolution |
|---|---|
| Two agents disagree on tone | Brand Intelligence decision applies |
| Output contradicts approved brand identity | Brand Guardian rejects; Source resets the flagged step |
| Tone mismatch between steps | Language Polisher resolves during its step |
| Structural inconsistency | Genesis Architect or System Orchestrator flags for Source |
| Legal ambiguity | Legal & Compliance Guard flags; no output published until resolved |

No agent resolves conflicts by overwriting another agent's approved output. Conflict resolution is surfaced to Source.

---

## 7. SUPPORT & EXTENSION LOGIC

Agents enhance each other's output through defined handoffs, not rewrites.

**Enhancement vs. override:**
- **Enhancement:** Adding precision, improving register, applying brand voice — permitted
- **Override:** Changing the substance, structure, or intent of an upstream artifact — not permitted without Source reset

**How agents add value without rewriting:**
- Humanizer applies voice and tone without altering the offer structure or funnel logic from Steps 1–2.
- Language Polisher adjusts word-level quality without changing the answer the Chat Agent constructed.
- Brand Guardian validates and assembles — it does not rewrite content that already passed upstream approval.

**Refinement is additive.** Each agent's output should be more complete, more precise, or more aligned than what it received — not a replacement of it.

---

## 8. FAILURE HANDLING

If an agent fails to produce output or produces an invalid output:

1. The failure is logged immediately in `logs/updates.log` with agent name, step, task ID, and error type.
2. The pipeline pauses at that step.
3. Source is notified via the log.
4. The agent does not attempt to retry without a Source-initiated reset.

**Fallback behavior:**
- If Brand Guardian fails: the pipeline pauses. No FINAL.md is assembled. No output is released.
- If Humanizer fails: Content Producer output is flagged as unhumanized. It is not passed to Brand Guardian.
- If Semantic Core fails in the communication pipeline: Chat Agent does not respond. It returns a neutral holding message pending re-interpretation.

**Minimal safe output rule:**
If a downstream agent receives incomplete input, it produces the portion it can complete, marks the incomplete sections clearly, and flags the output for Source review before advancing.

---

## 9. COMMUNICATION FORMAT BETWEEN AGENTS

All inter-agent output must follow this structured format. No raw or unstructured data is passed between agents.

### Standard Output Block

```
AGENT: [agent name]
STEP: [pipeline step number]
TASK: [task ID]
STATUS: [output | flagged | review_required]

INTERPRETED_INTENT: [what the upstream input means]
DECISION: [what this agent decided to produce]
TONE_INSTRUCTION: [tone and register applied]
OUTPUT_SUMMARY: [one sentence description of what was produced]
NEXT_AGENT: [which agent receives this output]
FLAGS: [any concerns, ambiguities, or required reviews — or NONE]
```

### File-based output (content pipeline)

All file outputs follow the naming convention: `logs/outputs/TASK-XXX/[step]-[type].md`

Each file begins with the agent header block above before the content begins.

### Real-time output (communication pipeline)

Chat Agent delivers the final user-facing message. Language Polisher and Navigation System outputs are embedded within that message — they do not generate separate visible artifacts.

---

## 10. HUMAN COHERENCE PRIORITY

The system produces outputs for humans.

**Human coherence overrides technical completeness.** If a technically correct response feels unnatural, the natural version is chosen.

**Applied across all agents:**
- Humanizer prioritizes voice over correctness of phrasing
- Chat Agent prioritizes clarity over completeness
- Language Polisher prioritizes flow over precise word accuracy
- Brand Guardian will flag outputs that are technically valid but feel robotic

**Conflict resolution when human coherence is at stake:**
If a technically correct output and a natural-sounding output are in conflict, the natural output is selected and the technical discrepancy is flagged — not hidden. Source decides whether to accept the flag or request a revision.

The system produces no output that a real person would feel is written by a machine.

---

## HARD CONSTRAINTS

- No agent may override an entire upstream artifact without a Source-initiated reset.
- No agent may act outside its defined role.
- No two agents may perform the same operation on the same artifact in the same pipeline step.
- No infinite loops. If an agent receives the same input twice, it logs a conflict and halts.
- No conflicting final outputs. The FINAL.md produced by Brand Guardian is the single authoritative output for any task.
- No output is published or delivered to users without completing the full pipeline and receiving Source approval.

---

## FAILURE CONDITIONS

The system is INVALID if:

- Two agents produce contradictory final outputs for the same task
- An agent modifies an upstream-approved artifact without Source permission
- A pipeline step is skipped
- The same responsibility is executed by two different agents
- An agent acts without its required upstream input
- A loop is detected in execution state

---

## SUCCESS CRITERIA

The system is SUCCESSFUL when:

- Each agent receives structured input, produces structured output, and passes it cleanly to the next step
- Outputs improve in precision and alignment at each step
- No two agents duplicate work
- The final artifact is coherent, brand-aligned, and human-voiced
- Source retains full control at every approval gate
- The system can be extended with new agents without restructuring the existing flow

---

## EXECUTION MODE

- **Structured** — every action follows a defined protocol
- **Deterministic** — the same inputs produce consistent outputs
- **Cooperative** — agents enhance, not compete with, each other
- **Non-competitive** — no agent attempts to produce output outside its scope
- **System-first** — the integrity of the pipeline takes precedence over any individual agent's output

---

> All agents operate as a coordinated system, where each one contributes its role without conflict, duplication, or disruption. The whole is more coherent than any part.
