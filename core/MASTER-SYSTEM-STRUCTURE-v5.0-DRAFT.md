# MASTER SYSTEM STRUCTURE v5.0 — DRAFT
# AurinBeyond / Genesis
# Status: DRAFT — Not yet approved as final authority
# Date: 2026-04-07

---

> **WARNING:** This file was reconstructed from existing repository evidence.
> It is NOT an authoritative source.
> No agent may treat this file as final authority until Section 9 (REQUIRED HUMAN APPROVAL) is completed by Source.
> AGENT-REGISTRY.md must NOT be created from this file until it has been explicitly approved by Source.

---

## SECTION 1 — PURPOSE

This file is a reconstruction draft created because the authoritative committed MASTER SYSTEM STRUCTURE v5.0 source was missing from the repository.

The authoritative version was referenced by name in `agents/ORCHESTRATOR-FLOW.md`
("Aligned to Master Structure v5.0") but was never committed to this repository.
Full-text search for "MASTER SYSTEM STRUCTURE" in the repository returned 0 matches before this file was created.
Full-text search for "v5.0" returned 1 match — only the title line of `agents/ORCHESTRATOR-FLOW.md`.

This file is NOT final authority yet.
This file exists to enable review and approval.
AGENT-REGISTRY.md must not be finalized until this draft is approved by Source.

This draft exists for one purpose:
**Give Source a concrete base to review, correct, and approve — so that AGENT-REGISTRY.md can be created.**

This file does NOT:
- invent agents
- assign layer numbers without evidence
- claim authority it does not have
- unblock the registry automatically

This file DOES:
- list every file consulted and what evidence it provided
- consolidate all scattered agent evidence into one place
- separate confirmed, inferred, and unresolved items
- provide an explicit alias/legacy name map
- identify exactly what human approval is needed before the registry can be created

---

## SECTION 2 — SOURCE EVIDENCE

All files scanned during reconstruction. Evidence is cited by source throughout this document.

| File | Evidence Type | Direct / Indirect | Key Content |
|---|---|---|---|
| `agents/ORCHESTRATOR-FLOW.md` | **Agent names, roles, aliases, pipeline order, activation status** | Direct | v5.0 name alignment table (9 active agents + 5 LATER agents); pipeline step sequence; handoff table; control rules |
| `agents/AGENTS-REGISTRY.md` | Agent IDs, roles, permissions, dependencies | Direct | 4 technical agents fully defined: GENESIS-ORCHESTRATOR, TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR |
| `agents/AGENT-BASE.md` | Agent types, lifecycle states, communication rules | Direct | Defines 4 agent type categories (Execution, Validation, Orchestrator, System); lifecycle states (IDLE→COMPLETE) |
| `agents/course-creator/agent.md` | Single agent definition | Direct | COURSE-CREATOR v1.1 — active definition file in /agents/ |
| `agents/AGENT-REGISTRY-BLOCKER-REPORT.md` | Prior reconstruction analysis, file inventory | Direct | Lists all files searched; confirms no v5.0 source exists; lists agent names scattered across repo |
| `AGENTS.md` | Core mission statement | Direct | Tone/voice protocol; agent access to `01-the-source-within.md`; no agent list |
| `AGENTS-CONFIG.md` | Active task with agent reference | Direct | TASKMASTER v1.7; `@LanguageAgent` referenced in HIGH PRIORITY active task |
| `TASKMASTER.md` | Active pipeline state | Direct | TASK-001 active; FUNNEL-ARCHITECT and OFFER-ARCHITECT named; 5-step pipeline described |
| `SYSTEM-ARCHITECTURE.md` | Architecture hierarchy, structural rules | Direct | TASKMASTER→ORCHESTRATOR→AGENT→OUTPUT hierarchy; agent system position; structural layer definitions |
| `SYSTEM-INDEX.md` | Repository structure map | Direct | Lists authorized directories; confirms `/agents/` structure |
| `SYSTEM_RULES.md` | Visual/brand rules | Indirect | No agent architecture; confirms Brand Guardian scope indirectly |
| `SYSTEM RULES v1.2` | Priority hierarchy (Estonian) | Direct | `CORE → LAWS → OPERATION → ORCHESTRATOR → AGENT`; BRIDGE role named; state model (draft/approved/locked) |
| `laws/GENESIS-OPERATION.md` | Operational execution rules | Direct | Agent autonomy model; handoff format; 90% autonomous execution; escalation triggers |
| `core/GENESIS-LAWS.md` | System laws | Indirect | Referenced as authority source; no agent list |
| `core/STATE.md` | State definitions | Indirect | Agent state values (IDLE, READY, ACTIVE, REVIEW, BLOCKED, FAILED, COMPLETE) |
| `core/MODE.md` | Mode definitions | Indirect | Agent mode values; no agent list |
| `core/INPUT.md` | Input validation rules | Indirect | No agent list |
| `core/OUTPUT-STANDARD.md` | Output standards | Indirect | No agent list |
| `core/TASK.md` | Task structure rules | Indirect | No agent list |
| `archive/agents-Agents-AGENT.md` | Old agent definition format | Indirect | Base behavior definition; no layer structure; archived |
| `archive/agents-agents-AGENTS.md` | Old agent list | Indirect | Single active agent: COURSE-CREATOR; no layer structure; archived |
| `archive/core-structure-plan.txt` | Old directory structure plan | Indirect | No agent list |
| `README.md` | Project description | Indirect | No agent definitions |
| `ARKANA-OS` | Estonian-language OS narrative | Indirect | No agent definitions; 6-node cognitive system flow described |

**Summary:**
- 24 files scanned
- Strongest evidence source: `agents/ORCHESTRATOR-FLOW.md` (v5.0 name alignment table)
- Zero files contain a committed authoritative layer-based agent registry
- Zero files explicitly declare themselves to be MASTER SYSTEM STRUCTURE v5.0

---

## SECTION 3 — CONFIRMED AGENTS

These agents are explicitly named with official v5.0 designations in `agents/ORCHESTRATOR-FLOW.md`.
That document's Section 1 ("Name Alignment Fixes") provides a mapping from previous names to
"Official v5.0 Names." This is the strongest direct evidence available in the repository.

Trigger and activation context are drawn from ORCHESTRATOR-FLOW.md Section 2 and the pipeline flow in Section 3.

### Active Pipeline Agents (9 agents — ACTIVE NOW):

---

**Agent 1: System Orchestrator**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed in name alignment table)
- Role: Reads TASKMASTER.md, assigns tasks, enforces sequence, triggers handoffs
- Activation trigger: Source adds task to TASKMASTER.md with status `pending`
- Stop condition: Task status is `review` — waits for Source approval
- Relationship: Controls all other agents; assigns one step at a time; only reads TASKMASTER.md
- Known aliases: GENESIS-ORCHESTRATOR (see Section 5)
- Layer: UNRESOLVED (see Section 8)

---

**Agent 2: Offer Architect**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed)
- Role: Defines products — name, transformation, format, price, audience
- Activation trigger: System Orchestrator assigns Step 1
- Stop condition: Output written to `logs/outputs/TASK-XXX/01-offer.md` — sets status REVIEW
- Relationship: Step 1 of pipeline → outputs to Funnel Architect
- Known aliases: OFFER-ARCHITECT (see Section 5)
- Layer: UNRESOLVED

---

**Agent 3: Funnel Architect**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed)
- Role: Defines sales flow — entry point, headline, problem statement, shift, offer, CTA
- Activation trigger: Source approves Step 1 output
- Stop condition: Output written to `logs/outputs/TASK-XXX/02-funnel.md` — sets status REVIEW
- Relationship: Step 2 of pipeline → receives from Offer Architect → outputs to Content Producer
- Known aliases: FUNNEL-ARCHITECT (see Section 5)
- Layer: UNRESOLVED

---

**Agent 4: Content Producer**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed)
- Role: Writes raw section copy based on approved funnel structure or page architecture
- Activation trigger: Source approves Step 2 output
- Stop condition: Output written to `logs/outputs/TASK-XXX/03-content.md` — sets status REVIEW
- Relationship: Step 3 of pipeline → receives from Funnel Architect or Genesis Architect → outputs to Humanizer
- Known aliases: CONTENT-PRODUCER, COPY-AGENT (see Section 5)
- Layer: UNRESOLVED

---

**Agent 5: Humanizer**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed; explicitly labeled MANDATORY, no exceptions)
- Role: Transforms raw agent output into brand-consistent, human-voice copy. Removes AI patterns.
- Activation trigger: Source approves Step 3 output
- Stop condition: Output written to `logs/outputs/TASK-XXX/04-humanized.md` — sets status REVIEW
- Relationship: Step 4 of pipeline — MANDATORY on every task → receives from Content Producer → outputs to Brand Guardian
- Known aliases: HUMANIZER (unchanged — already official per ORCHESTRATOR-FLOW.md)
- Layer: UNRESOLVED

---

**Agent 6: Brand Guardian**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed; explicitly labeled MANDATORY, no exceptions)
- Role: Validates all content against brand identity (tone, values, visual rules); assembles FINAL.md
- Activation trigger: Source approves Step 4 output
- Stop condition: FINAL.md assembled — sets status REVIEW
- Relationship: Step 5 of pipeline — MANDATORY on every task; final gate before Source release decision
- Known aliases: BRAND-GUARDIAN (see Section 5)
- Layer: UNRESOLVED

---

**Agent 7: Genesis Architect**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed; replaces PAGE-ARCHITECT)
- Role: Defines page structure (sections, hierarchy, flow) for each site page — no copy, no code
- Activation trigger: Offer or book/course definition approved by Source
- Stop condition: Structure doc complete — passes to Content Producer
- Relationship: Standalone task; output feeds Content Producer
- Known aliases: PAGE-ARCHITECT (see Section 5)
- Layer: UNRESOLVED

---

**Agent 8: Frequency Transmitter**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed; replaces TRUST-LAYER-AGENT)
- Role: Builds authority content — about page, proof, credentials, testimony structure; transmits the Genesis signal
- Activation trigger: Core offers defined and approved
- Stop condition: Drafts in REVIEW
- Relationship: Standalone task; produces trust/authority layer content
- Known aliases: TRUST-LAYER-AGENT (see Section 5)
- Layer: UNRESOLVED

---

**Agent 9: Legal & Compliance Guard**
- Evidence: `agents/ORCHESTRATOR-FLOW.md` (official name confirmed; replaces LEGAL-AGENT)
- Role: Produces legal pages — Terms, Privacy, Disclaimer — based on offer type and jurisdiction
- Activation trigger: Offer ecosystem defined
- Stop condition: Legal drafts in REVIEW
- Relationship: Standalone task; no dependency on content pipeline
- Known aliases: LEGAL-AGENT (see Section 5)
- Layer: UNRESOLVED

---

### Confirmed Future Agents (5 agents — marked LATER in ORCHESTRATOR-FLOW.md):

| # | Official Name | Known Previous Name | Planned Phase | Source |
|---|---|---|---|---|
| 10 | Community Catalyst | COMMUNITY-AGENT | After core site is live | `agents/ORCHESTRATOR-FLOW.md` |
| 11 | Visual Director | — | Design/visual production phase | `agents/ORCHESTRATOR-FLOW.md` |
| 12 | Language Polisher & Adapter | — | Localization/adaptation phase | `agents/ORCHESTRATOR-FLOW.md` |
| 13 | Integrity Auditor | — | Full system audit post-launch | `agents/ORCHESTRATOR-FLOW.md` |
| 14 | Product Delivery System | — | Delivery infrastructure phase | `agents/ORCHESTRATOR-FLOW.md` |

**Source of confirmation for all 14 agents:** `agents/ORCHESTRATOR-FLOW.md` — the v5.0 name alignment table, Section 2 (active agent definitions), and Section 4 (role mapping check).

---

## SECTION 4 — INFERRED AGENTS

These agents appear in repository files but are NOT in the ORCHESTRATOR-FLOW.md v5.0 name-aligned list.
Their relationship to the official v5.0 structure is unclear.

---

**Inferred Agent T1: GENESIS-ORCHESTRATOR**
- Source: `agents/AGENTS-REGISTRY.md`
- Why inferred: Has a full AGENT_ID definition with ROLE, SCOPE, PERMISSIONS, DEPENDENCIES. Pre-dates the v5.0 pipeline naming. Likely the technical ID for "System Orchestrator" but this is not confirmed anywhere.
- What is uncertain: Whether this is the same entity as System Orchestrator (v5.0 name) or a distinct system-layer agent.
- Status: INFERRED — requires human approval

---

**Inferred Agent T2: TASK-EXECUTOR**
- Source: `agents/AGENTS-REGISTRY.md`
- Why inferred: Fully defined with AGENT_ID, ROLE (Execute defined tasks), SCOPE, PERMISSIONS, DEPENDENCIES. No counterpart in ORCHESTRATOR-FLOW.md v5.0 agent list.
- What is uncertain: Whether this agent is still active, whether it was superseded by the content pipeline agents, or whether it operates at a different layer (system execution vs. content production).
- Status: INFERRED — requires human approval

---

**Inferred Agent T3: OUTPUT-VALIDATOR**
- Source: `agents/AGENTS-REGISTRY.md`
- Why inferred: Fully defined with AGENT_ID, ROLE (Validate outputs), SCOPE, PERMISSIONS, DEPENDENCIES. No counterpart in ORCHESTRATOR-FLOW.md v5.0 agent list.
- What is uncertain: Whether Brand Guardian (v5.0) absorbed this role, or whether OUTPUT-VALIDATOR remains a separate infrastructure-level agent.
- Status: INFERRED — requires human approval

---

**Inferred Agent T4: SYSTEM-AUDITOR**
- Source: `agents/AGENTS-REGISTRY.md`
- Why inferred: Fully defined with AGENT_ID, ROLE (Ensure system integrity), SCOPE, PERMISSIONS, DEPENDENCIES. Most closely maps to Integrity Auditor (v5.0 LATER) but is not confirmed as the same agent.
- What is uncertain: Whether this is an early version of Integrity Auditor or a permanent infrastructure-level agent that will coexist with it.
- Status: INFERRED — requires human approval

---

**Inferred Agent A1: COURSE-CREATOR**
- Source: `agents/course-creator/agent.md` (v1.1), `archive/agents-agents-AGENTS.md`
- Why inferred: The only agent with a live definition file in `/agents/`. Not archived. Not present in ORCHESTRATOR-FLOW.md v5.0 agent list. May be a pre-v5.0 content agent that predates the current pipeline, or a standalone agent for course production not covered by the 5-step pipeline.
- What is uncertain: Whether it is a v5.0 agent requiring an official name, or a legacy agent to be archived.
- Status: INFERRED — requires human approval

---

**Inferred Agent U1: @LanguageAgent**
- Source: `AGENTS-CONFIG.md` (TASKMASTER v1.7, active HIGH PRIORITY task)
- Why inferred: Referenced as the executing agent for an active HIGH PRIORITY task. No definition file. No registry entry. No v5.0 name alignment. Could be Language Polisher & Adapter (v5.0 LATER name) or a completely separate agent.
- What is uncertain: Identity, scope, and whether this task should be reassigned to a registered agent.
- Status: INFERRED — requires human approval. Active HIGH PRIORITY task is currently blocked by this uncertainty.

---

**Inferred Role: BRIDGE**
- Source: `SYSTEM RULES v1.2` (Estonian-language file)
- Why inferred: Named in the system separation rules: "BRIDGE ei otsusta strateegiat" (BRIDGE does not decide strategy). No agent with this name or role exists anywhere else in the repository.
- What is uncertain: Whether BRIDGE is an agent, a system concept, an integration layer name, or a deprecated term from an earlier version of the system.
- Status: INFERRED — requires human approval

---

## SECTION 5 — LEGACY / ALIAS NAME MAP

This table maps all unofficial, legacy, or scattered agent names to their probable official v5.0 names.
Source for all HIGH-confidence mappings: `agents/ORCHESTRATOR-FLOW.md` Section 1 (Name Alignment Fixes), which explicitly states "Previous Name → Official v5.0 Name."

| Legacy / Unofficial Name | Probable Official v5.0 Name | Confidence | Evidence |
|---|---|---|---|
| GENESIS-ORCHESTRATOR | System Orchestrator | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| OFFER-ARCHITECT | Offer Architect | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| FUNNEL-ARCHITECT | Funnel Architect | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| CONTENT-PRODUCER | Content Producer | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| COPY-AGENT | Content Producer | HIGH | ORCHESTRATOR-FLOW.md Section 1: "Consolidated under Content Producer" |
| HUMANIZER | Humanizer | HIGH | ORCHESTRATOR-FLOW.md Section 1: "Unchanged — already official" |
| BRAND-GUARDIAN | Brand Guardian | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| PAGE-ARCHITECT | Genesis Architect | HIGH | ORCHESTRATOR-FLOW.md Section 1: "Site/page structure = Genesis Architect scope" |
| TRUST-LAYER-AGENT | Frequency Transmitter | HIGH | ORCHESTRATOR-FLOW.md Section 1: "Authority/about content = frequency transmission" |
| LEGAL-AGENT | Legal & Compliance Guard | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| COMMUNITY-AGENT | Community Catalyst | HIGH | ORCHESTRATOR-FLOW.md Section 1 explicit mapping |
| SEWING-COURSE-AGENT | NOT USED — removed | HIGH | ORCHESTRATOR-FLOW.md Section 1: "External / separate brand — removed from registry" |
| CHILDREN-SECTION-AGENT | (future work — no agent assigned yet) | HIGH | ORCHESTRATOR-FLOW.md Section 1: "Marked LATER — no active assignment yet" |
| TASK-EXECUTOR | Unknown — possibly no v5.0 equivalent | LOW | Found only in `agents/AGENTS-REGISTRY.md`; no mapping in ORCHESTRATOR-FLOW.md |
| OUTPUT-VALIDATOR | Unknown — possibly Brand Guardian or Integrity Auditor | LOW | Found only in `agents/AGENTS-REGISTRY.md`; no mapping in ORCHESTRATOR-FLOW.md |
| SYSTEM-AUDITOR | Possibly Integrity Auditor | LOW | Similar role description; not confirmed |
| COURSE-CREATOR | Unknown — possibly Content Producer or standalone | LOW | Active file in `/agents/`; no v5.0 name assigned anywhere |
| @LanguageAgent | Possibly Language Polisher & Adapter | LOW | Name similarity only; no confirmation |
| BRIDGE | Unknown | LOW | Named in SYSTEM RULES v1.2 only; no counterpart anywhere |

**Note on HIGH-confidence mappings:** These are directly stated in ORCHESTRATOR-FLOW.md. They are not inferred.
**Note on LOW-confidence mappings:** These are name-similarity guesses only. Do not treat them as confirmed.

---

## SECTION 6 — LAYER MODEL DRAFT

**⚠️ This section is entirely inferred. No layer numbers exist in any repository file.**

The following is reconstructed from:
- Priority hierarchy in `SYSTEM RULES v1.2`: `CORE → LAWS → OPERATION → ORCHESTRATOR → AGENT`
- Structural logic of `laws/GENESIS-OPERATION.md`
- Agent type categories in `agents/AGENT-BASE.md` (Execution, Validation, Orchestrator, System)
- Pipeline step order in `agents/ORCHESTRATOR-FLOW.md`
- Architecture hierarchy in `SYSTEM-ARCHITECTURE.md`: `TASKMASTER → ORCHESTRATOR → AGENT → OUTPUT`

```
LAYER 0 — CORE SYSTEM (laws, state, input/output rules)
  Confidence: PARTIAL — layer concept is evidenced, number "0" is inferred
  Files: core/GENESIS-LAWS.md, core/STATE.md, core/MODE.md, core/INPUT.md, core/OUTPUT-STANDARD.md
  Agents: none — this is the rule layer, not an execution layer

LAYER I — OPERATIONAL LAWS
  Confidence: PARTIAL — layer concept is evidenced, numbering is inferred
  Files: laws/GENESIS-OPERATION.md
  Agents: none — this is the execution rules layer

LAYER II — ORCHESTRATION
  Confidence: PARTIAL — orchestration as a distinct layer is confirmed; exact numbering is inferred
  Agent: System Orchestrator (Official v5.0) / GENESIS-ORCHESTRATOR (legacy technical ID)
  Role: reads TASKMASTER, assigns tasks, enforces sequence, triggers handoffs
  Note: SYSTEM-ARCHITECTURE.md confirms ORCHESTRATOR sits between TASKMASTER and AGENT layers

LAYER III — SYSTEM/INFRASTRUCTURE AGENTS
  Confidence: UNRESOLVED — these agents exist in AGENTS-REGISTRY.md but their layer is not stated
  Agents: TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR (inferred — see Section 4)
  Role: system-level execution, validation, audit

LAYER IV — CONTENT PIPELINE AGENTS (ACTIVE NOW)
  Confidence: PARTIAL — the pipeline step order is confirmed; the layer number is inferred
  Agents: Offer Architect (Step 1), Funnel Architect (Step 2), Content Producer (Step 3),
          Humanizer (Step 4 — mandatory), Brand Guardian (Step 5 — mandatory)
  Role: 5-step content production pipeline; sequential; each step requires Source approval

LAYER V — ARCHITECTURE & AUTHORITY AGENTS (ACTIVE NOW)
  Confidence: PARTIAL — standalone task status is confirmed; grouping as a layer is inferred
  Agents: Genesis Architect, Frequency Transmitter, Legal & Compliance Guard
  Role: standalone task execution for site structure, authority content, and legal pages

LAYER VI — COMMUNITY & GROWTH AGENTS (LATER)
  Confidence: UNRESOLVED — activation phase is confirmed LATER; layer grouping is inferred
  Agents: Community Catalyst
  Role: community engagement, newsletter, contact flow

LAYER VII — QUALITY & LOCALIZATION AGENTS (LATER)
  Confidence: UNRESOLVED — activation phase is confirmed LATER; layer grouping is inferred
  Agents: Language Polisher & Adapter, Integrity Auditor
  Role: localization, full system audit post-launch

LAYER VIII — VISUAL & DELIVERY AGENTS (LATER)
  Confidence: UNRESOLVED — activation phase is confirmed LATER; layer grouping is inferred
  Agents: Visual Director, Product Delivery System
  Role: visual production, delivery infrastructure

LAYER IX — UNCLASSIFIED / LEGACY
  Confidence: UNRESOLVED — these agents exist but have no confirmed v5.0 classification
  Agents: COURSE-CREATOR (active file, no v5.0 assignment), @LanguageAgent (task reference, undefined),
          BRIDGE (role name, undefined)
  Role: unclear — requires human classification decision
```

**Overall confidence rating of this layer model:** LOW.
These are inferred groupings only. No source file confirms this structure or these numbers.
Layer numbers (0, I, II, etc.) are a reconstruction hypothesis, not confirmed design.

---

## SECTION 7 — SYSTEM HIERARCHY DRAFT

This section reconstructs the intended execution flow from available evidence.
Sources: `SYSTEM-ARCHITECTURE.md`, `agents/ORCHESTRATOR-FLOW.md`, `TASKMASTER.md`, `laws/GENESIS-OPERATION.md`.

### Confirmed Top-Level Flow:

```
SOURCE (human / AurinBeyond)
  └─ adds task to TASKMASTER.md (status: pending)
       │
       ▼
TASKMASTER.md
  └─ single source of all task input (confirmed: laws/GENESIS-OPERATION.md, SYSTEM-ARCHITECTURE.md)
       │
       ▼
System Orchestrator
  └─ reads task from TASKMASTER.md
  └─ assigns to Step 1 agent
  └─ enforces sequence
  └─ triggers handoffs between steps
       │
       ▼
CONTENT PIPELINE (5-step, sequential — confirmed: ORCHESTRATOR-FLOW.md)
  │
  ├─ STEP 1 — Offer Architect
  │    └─ output: logs/outputs/TASK-XXX/01-offer.md → status: REVIEW
  │    └─ [Source approves]
  │
  ├─ STEP 2 — Funnel Architect
  │    └─ input: approved 01-offer.md
  │    └─ output: logs/outputs/TASK-XXX/02-funnel.md → status: REVIEW
  │    └─ [Source approves]
  │
  ├─ STEP 3 — Content Producer
  │    └─ input: approved 02-funnel.md (or page structure from Genesis Architect)
  │    └─ output: logs/outputs/TASK-XXX/03-content.md → status: REVIEW
  │    └─ [Source approves]
  │
  ├─ STEP 4 — Humanizer  [MANDATORY — no exceptions]
  │    └─ input: approved 03-content.md
  │    └─ output: logs/outputs/TASK-XXX/04-humanized.md → status: REVIEW
  │    └─ [Source approves]
  │
  └─ STEP 5 — Brand Guardian  [MANDATORY — no exceptions]
       └─ input: all approved step outputs for this task
       └─ output: logs/outputs/TASK-XXX/FINAL.md → status: REVIEW
       └─ [Source approves → moves task to COMPLETED]
            │
            ▼
         OUTPUT: FINAL.md (approved and logged)
```

### Standalone Task Agents (confirmed: ORCHESTRATOR-FLOW.md — run outside the 5-step pipeline):

```
Source-approved trigger
  │
  ├─ Genesis Architect
  │    └─ Defines page structure → passes to Content Producer
  │
  ├─ Frequency Transmitter
  │    └─ Produces authority / trust layer content (about page, proof, credentials)
  │
  └─ Legal & Compliance Guard
       └─ Produces legal pages (Terms, Privacy, Disclaimer)
```

### Future Agents (confirmed LATER — not yet active):

```
After core site is live:
  └─ Community Catalyst

Post-launch phases:
  └─ Visual Director (design/visual production)
  └─ Language Polisher & Adapter (localization)
  └─ Integrity Auditor (full system audit)
  └─ Product Delivery System (delivery infrastructure)
```

### System Control Rules (confirmed: ORCHESTRATOR-FLOW.md):

- Only Source sets task status to DONE
- No agent marks a task DONE
- No agent skips steps
- No agent overwrites an existing step file
- System Orchestrator assigns one step at a time — no parallel execution
- Output moves forward only — no step re-executed unless Source explicitly resets it
- Source approval required between every step

### Unconfirmed Hierarchy Items (inferred — see Section 8):

```
AGENTS-REGISTRY.md defines a parallel infrastructure layer:
  System Orchestrator (GENESIS-ORCHESTRATOR)
    └─ TASK-EXECUTOR (executes tasks)
    └─ OUTPUT-VALIDATOR (validates outputs)
    └─ SYSTEM-AUDITOR (system integrity)

Relationship of this infrastructure layer to the content pipeline is UNRESOLVED.
```

---

## SECTION 8 — UNRESOLVED ITEMS

Every missing or unclear item is listed below. This section is complete and unambiguous.

| # | Unresolved Item | Why Unresolved | Impact on Registry |
|---|---|---|---|
| U1 | Official v5.0 agent count | No source file states total agent count. ORCHESTRATOR-FLOW.md lists 14 agents (9 active + 5 LATER) but never declares "total = 14" as the authoritative count. | Cannot verify registry completeness |
| U2 | Layer numbers | No file assigns Layer 0 through Layer IX (or any other numbering) to specific agents. The layer model in Section 6 is inferred hypothesis. | Layer assignments in registry would be fabricated |
| U3 | COURSE-CREATOR classification | COURSE-CREATOR v1.1 exists in `/agents/course-creator/agent.md` — an active, non-archived file. It does not appear in the ORCHESTRATOR-FLOW.md v5.0 agent list. Classification is unknown: is it a v5.0 agent needing an official name, or a legacy agent to be archived? | Cannot include or exclude from registry without decision |
| U4 | @LanguageAgent identity | Appears in an active HIGH PRIORITY task in AGENTS-CONFIG.md. No definition file, no registry entry. Could be Language Polisher & Adapter (v5.0 LATER) or a distinct unregistered agent. HIGH PRIORITY task is currently unexecutable. | Active task blocked; cannot route task without agent identity |
| U5 | TASK-EXECUTOR status | Fully defined in AGENTS-REGISTRY.md. Not in v5.0 pipeline. Is it still active, superseded, or operating at a different layer? | Risk of double entry if not resolved |
| U6 | OUTPUT-VALIDATOR status | Fully defined in AGENTS-REGISTRY.md. Not in v5.0 pipeline. Brand Guardian may absorb this role, but this is not stated. | Risk of double entry if not resolved |
| U7 | SYSTEM-AUDITOR vs. Integrity Auditor | SYSTEM-AUDITOR is defined in AGENTS-REGISTRY.md; Integrity Auditor is in v5.0 LATER list. Are they the same agent with different names, or two distinct agents? | Duplicate or missing entry risk |
| U8 | BRIDGE role | Named in SYSTEM RULES v1.2 only. No counterpart anywhere else. Agent, concept, or deprecated term? | Unknown scope — may be missing agent |
| U9 | Children's section agent | ORCHESTRATOR-FLOW.md marks this as "Future work — no agent assigned yet." No agent name assigned. | Unregistered future need — cannot be in registry without name |
| U10 | Official agent ID format | v5.0 uses human-readable names (System Orchestrator). AGENTS-REGISTRY.md uses ALL-CAPS IDs (GENESIS-ORCHESTRATOR). Which format is authoritative? Or does v5.0 use both (display name + technical ID)? | Registry requires consistent ID format |
| U11 | Whether v5.0 supersedes AGENTS-REGISTRY.md | AGENTS-REGISTRY.md defines 4 technical agents. ORCHESTRATOR-FLOW.md defines 14 pipeline agents. Are these parallel systems or does v5.0 entirely replace the earlier technical layer? | Determines registry architecture |
| U12 | Official document for MASTER SYSTEM STRUCTURE v5.0 | The document referenced by this name was never committed. This draft is the reconstruction attempt. | The gap this file was created to address |

---

## SECTION 9 — REQUIRED HUMAN APPROVAL

The following items must be reviewed and decided by Source before this draft can become
`core/MASTER-SYSTEM-STRUCTURE-v5.0.md` (final authority).

### 9.1 Official Agent Count
> What is the official total number of agents in MASTER SYSTEM STRUCTURE v5.0?
> Current reconstruction: 14 named agents (9 active + 5 LATER).
> Confirm this count or provide the correct number.

### 9.2 Layer Assignments
> Does a layer model (Layer 0 → Layer IX or similar) exist in the intended design?
> If yes: assign each confirmed agent to its layer. The draft in Section 6 can be used as a starting point.
> If no: confirm that layers are not part of v5.0 and this field should be removed from the registry.

### 9.3 Official Agent ID Format
> What is the official agent ID format for v5.0?
> Option A: Human-readable display name only (System Orchestrator, Offer Architect)
> Option B: ALL-CAPS technical ID only (GENESIS-ORCHESTRATOR, OFFER-ARCHITECT)
> Option C: Both — human-readable display name + ALL-CAPS technical ID

### 9.4 COURSE-CREATOR Classification
> Is COURSE-CREATOR a v5.0 agent requiring an official name and layer assignment?
> Or is it a pre-v5.0 legacy agent to be archived?

### 9.5 @LanguageAgent Identity
> Is @LanguageAgent the same agent as Language Polisher & Adapter (v5.0 LATER)?
> Or is it a separate, currently unregistered agent?
> Decision needed: the HIGH PRIORITY active task in AGENTS-CONFIG.md is currently unexecutable.

### 9.6 Infrastructure Agents Status (TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR)
> Do these three agents remain active in v5.0 as infrastructure-level agents?
> Or are they superseded by pipeline agents (Brand Guardian, Integrity Auditor, etc.)?

### 9.7 BRIDGE Role
> What is BRIDGE (from SYSTEM RULES v1.2)?
> Is it an agent, a system concept, or a deprecated term?
> If it is an agent — provide its official v5.0 name.

### 9.8 Alias Decisions for LOW-confidence Mappings
> Review the LOW-confidence alias entries in Section 5 and confirm or correct each mapping.

### 9.9 Final Authority Confirmation
> Once all above questions are answered and this document is corrected to match the intended design,
> Source must explicitly state:
>
> **"MASTER SYSTEM STRUCTURE v5.0-DRAFT is approved as the source for AGENT-REGISTRY.md"**
>
> This statement is the required unblock condition.
> No agent may treat this file as final authority before this statement is made.

---

## SECTION 10 — NEXT STEP TO ENABLE AGENT-REGISTRY.md

AGENT-REGISTRY.md may only be created after:

1. This draft is reviewed by Source
2. All unresolved items in Section 8 are decided
3. This file is approved as final authority (Section 9.9 confirmation)

```
Step 1 — Source reviews this DRAFT
  └─ Answer all questions in Section 9
  └─ Correct any errors in Sections 3, 4, 5, 6, 7

Step 2 — Source approves this document
  └─ Explicit approval statement required (see Section 9.9)
  └─ Rename this file from DRAFT to approved:
       core/MASTER-SYSTEM-STRUCTURE-v5.0-DRAFT.md → core/MASTER-SYSTEM-STRUCTURE-v5.0.md

Step 3 — Create agents/AGENT-REGISTRY.md
  └─ Use only this approved document as the source
  └─ Every agent entry must trace to Section 3 or Section 4 of this document (after corrections)
  └─ Do not invent agents not present in the approved document
  └─ Do not create registry entries for unresolved items from Section 8
  └─ Format, layer assignments, and IDs must match Source-approved decisions from Section 9

Step 4 — Archive the blocker report
  └─ Move agents/AGENT-REGISTRY-BLOCKER-REPORT.md to /archive/
  └─ The blocker report is superseded once the registry is created and validated
```

**Until Step 2 is complete: AGENT-REGISTRY.md will not be created.**

---

*This file was produced by source reconstruction only.*
*No agents were invented. No authority was fabricated. No IDs were guessed.*
*All evidence cited traces to specific files in this repository.*
*Reconstruction date: 2026-04-07*
