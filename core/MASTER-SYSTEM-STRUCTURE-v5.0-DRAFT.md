# MASTER SYSTEM STRUCTURE v5.0 — DRAFT
# AurinBeyond / Genesis
# Date: 2026-04-07
# Status: ⚠️ DRAFT — SOURCE RECONSTRUCTION ONLY
# Authority: NOT VALIDATED — requires human review and explicit approval before use

---

> **WARNING:** This file was reconstructed from existing repository evidence.
> It is NOT an authoritative source.
> No agent may treat this file as final authority until Section 7 (REQUIRED HUMAN APPROVAL) is completed.
> AGENT-REGISTRY.md must NOT be created from this file until it has been explicitly approved by Source.

---

## SECTION 1 — PURPOSE

This file is a reconstruction attempt of the intended MASTER SYSTEM STRUCTURE v5.0.

The authoritative version of this document was referenced by name in `agents/ORCHESTRATOR-FLOW.md`
("Aligned to Master Structure v5.0") but was never committed to this repository.

This draft exists for one purpose:
**Give Source a concrete base to review, correct, and approve — so that AGENT-REGISTRY.md can be created.**

This file does NOT:
- invent agents
- assign layer numbers without evidence
- claim authority it does not have
- unblock the registry automatically

This file DOES:
- consolidate all scattered agent evidence into one place
- separate confirmed, inferred, and unresolved items
- identify exactly what human approval is needed

---

## SECTION 2 — STATUS

| Field | Value |
|---|---|
| Document version | v5.0-DRAFT |
| Reconstruction date | 2026-04-07 |
| Source files scanned | 24 files (see AGENT-REGISTRY-BLOCKER-REPORT.md for full list) |
| Confirmed agent names found | 14 (from ORCHESTRATOR-FLOW.md Section 1) |
| Technical/infrastructure agents | 4 (from AGENTS-REGISTRY.md) |
| Archived agents | 1 (COURSE-CREATOR) |
| Layer assignments confirmed | 0 |
| Authoritative source document found | NO |
| Ready to create AGENT-REGISTRY.md | NO — pending Section 7 approval |

---

## SECTION 3 — CONFIRMED AGENTS

These agents are explicitly named with official v5.0 designations in `agents/ORCHESTRATOR-FLOW.md`.
That document states "Section 1 — Name Alignment Fixes" and provides a mapping from previous names to
"Official v5.0 Names." This is the strongest evidence available in the repository.

### Active Pipeline Agents (confirmed in ORCHESTRATOR-FLOW.md Section 2 and 4):

| # | Official Name | Previous Name(s) | Role (from ORCHESTRATOR-FLOW.md) | Pipeline Status |
|---|---|---|---|---|
| 1 | System Orchestrator | GENESIS-ORCHESTRATOR | Reads TASKMASTER.md, assigns tasks, enforces sequence, triggers handoffs | ACTIVE NOW |
| 2 | Offer Architect | OFFER-ARCHITECT | Defines products: name, transformation, format, price, audience | ACTIVE NOW — Step 1 |
| 3 | Funnel Architect | FUNNEL-ARCHITECT | Defines sales flow: entry, headline, problem, shift, offer, CTA | ACTIVE NOW — Step 2 |
| 4 | Content Producer | CONTENT-PRODUCER, COPY-AGENT | Writes raw section copy based on approved funnel structure | ACTIVE NOW — Step 3 |
| 5 | Humanizer | HUMANIZER | Transforms raw output into brand-consistent, human-voice copy | ACTIVE NOW — Step 4 (mandatory) |
| 6 | Brand Guardian | BRAND-GUARDIAN | Validates all content against brand identity; assembles FINAL.md | ACTIVE NOW — Step 5 (mandatory) |
| 7 | Genesis Architect | PAGE-ARCHITECT | Defines page structure (sections, hierarchy, flow) for site pages | ACTIVE NOW — standalone task |
| 8 | Frequency Transmitter | TRUST-LAYER-AGENT | Builds authority content: about, proof, credentials, testimony structure | ACTIVE NOW — standalone task |
| 9 | Legal & Compliance Guard | LEGAL-AGENT | Produces legal pages: Terms, Privacy, Disclaimer | ACTIVE NOW — standalone task |

### Confirmed Future Agents (named in ORCHESTRATOR-FLOW.md, marked LATER):

| # | Official Name | Previous Name(s) | Planned Phase | Status |
|---|---|---|---|---|
| 10 | Community Catalyst | COMMUNITY-AGENT | After core site is live | LATER |
| 11 | Visual Director | — | Design/visual production phase | LATER |
| 12 | Language Polisher & Adapter | — | Localization/adaptation phase | LATER |
| 13 | Integrity Auditor | — | Full system audit post-launch | LATER |
| 14 | Product Delivery System | — | Delivery infrastructure phase | LATER |

**Source of confirmation:** `agents/ORCHESTRATOR-FLOW.md` — the v5.0 name alignment table and active agent definitions.

---

## SECTION 4 — INFERRED AGENTS

These agents appear in repository files but are NOT in the v5.0 name-aligned list.
Their relationship to the official v5.0 structure is unclear.

### Technical/Infrastructure Agents (from `agents/AGENTS-REGISTRY.md`):

These four agents have full AGENT_ID, ROLE, SCOPE, PERMISSIONS, and DEPENDENCIES definitions.
They appear to be a system-layer infrastructure set, separate from the pipeline agents above.

| # | Agent ID | Role | Source File |
|---|---|---|---|
| T1 | GENESIS-ORCHESTRATOR | Task coordination and system control | `agents/AGENTS-REGISTRY.md` |
| T2 | TASK-EXECUTOR | Execute defined tasks | `agents/AGENTS-REGISTRY.md` |
| T3 | OUTPUT-VALIDATOR | Validate outputs | `agents/AGENTS-REGISTRY.md` |
| T4 | SYSTEM-AUDITOR | Ensure system integrity | `agents/AGENTS-REGISTRY.md` |

**Note:** GENESIS-ORCHESTRATOR (T1) appears to be the technical ID for what the pipeline calls "System Orchestrator."
Whether T2, T3, T4 are standalone agents or sub-functions of the pipeline agents is not stated anywhere.

### Operational Roles (from `SYSTEM RULES v1.2`, Estonian-language file):

The file defines a priority hierarchy: `CORE → LAWS → OPERATION → ORCHESTRATOR → AGENT`

And names these roles:
- CORE — does not produce content
- AGENT — does not control the system
- BRIDGE — does not decide strategy *(relationship to any specific agent: unknown)*
- TASKMASTER — does not write prompts *(system file, not an agent)*
- OUTPUT-STANDARD — does not change content meaning *(system file, not an agent)*
- ORCHESTRATOR — determines sequence and handoffs only

**Inference:** The hierarchy in SYSTEM RULES v1.2 suggests a layer model, but no explicit layer numbers are assigned.

### Active Agent in Repository File Structure:

| # | Agent | Location | Version |
|---|---|---|---|
| A1 | COURSE-CREATOR | `agents/course-creator/agent.md` | v1.1 — active file in /agents/ |

**Note:** COURSE-CREATOR is the only agent with a live definition file under `/agents/`. Its relationship to the
v5.0 pipeline agent set is not stated. It is neither in the ORCHESTRATOR-FLOW.md active list nor in the archive list.
It may be a pre-v5.0 legacy agent or a standalone agent not part of the main pipeline.

### Unregistered Task Reference:

| # | Name | Source | Status |
|---|---|---|---|
| U1 | @LanguageAgent | `AGENTS-CONFIG.md` (TASKMASTER v1.7) | Active task assigned but not defined anywhere |

**Note:** `@LanguageAgent` appears in an active task in AGENTS-CONFIG.md with status HIGH PRIORITY.
No definition file, no registry entry, no v5.0 name alignment for this agent exists.

---

## SECTION 5 — LAYER MODEL DRAFT

**⚠️ This section is entirely inferred. No layer numbers exist in any repository file.**

The following is reconstructed from the priority hierarchy in `SYSTEM RULES v1.2` and the structural
logic of `laws/GENESIS-OPERATION.md` and `agents/AGENTS-REGISTRY.md`.

```
LAYER 0 — CORE SYSTEM (laws, state, input/output rules)
  Files: core/GENESIS-LAWS.md, core/STATE.md, core/MODE.md, core/INPUT.md, core/OUTPUT-STANDARD.md
  Agents: none — this is the rule layer

LAYER I — OPERATIONAL LAWS
  Files: laws/GENESIS-OPERATION.md, SYSTEM-LAWS (future)
  Agents: none — this is the execution rules layer

LAYER II — ORCHESTRATION
  Agent: System Orchestrator (Official) / GENESIS-ORCHESTRATOR (Technical ID)
  Role: reads tasks, assigns agents, enforces sequence

LAYER III — SYSTEM/INFRASTRUCTURE AGENTS (inferred)
  Agents: TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR
  Role: system-level execution, validation, audit

LAYER IV — CONTENT PIPELINE AGENTS (ACTIVE NOW)
  Agents: Offer Architect, Funnel Architect, Content Producer, Humanizer, Brand Guardian
  Role: 5-step content pipeline

LAYER V — ARCHITECTURE & AUTHORITY AGENTS (ACTIVE NOW)
  Agents: Genesis Architect, Frequency Transmitter, Legal & Compliance Guard
  Role: standalone task execution for site structure, authority, and legal

LAYER VI — COMMUNITY & GROWTH AGENTS (LATER)
  Agents: Community Catalyst
  Role: community engagement, newsletter, contact flow

LAYER VII — QUALITY & LOCALIZATION AGENTS (LATER)
  Agents: Language Polisher & Adapter, Integrity Auditor
  Role: localization, full system audit

LAYER VIII — VISUAL & DELIVERY AGENTS (LATER)
  Agents: Visual Director, Product Delivery System
  Role: visual production, delivery infrastructure

LAYER IX — UNCLASSIFIED / LEGACY
  Agents: COURSE-CREATOR (active but unassigned in v5.0), @LanguageAgent (unregistered reference)
  Role: unclear — requires human classification
```

**Confidence rating of this layer model:** LOW.
These are inferred groupings only. No source file confirms this structure.

---

## SECTION 6 — UNRESOLVED ITEMS

The following specific questions cannot be answered from existing repository evidence:

| # | Item | Why Unresolved | Impact |
|---|---|---|---|
| U1 | Official v5.0 agent count | No source file states total agent count. ORCHESTRATOR-FLOW.md lists 14 agents by name (9 active + 5 later) but never states "total = 14" as an official count. | Cannot verify completeness of any registry |
| U2 | Layer numbers | No file assigns Layer 0 through Layer IX to specific agents. The layer model in Section 5 is inferred. | Layer assignments in registry would be fabricated |
| U3 | COURSE-CREATOR classification | agent.md exists in `/agents/course-creator/` (v1.1, not archived) but COURSE-CREATOR does not appear in ORCHESTRATOR-FLOW.md v5.0 agent list. Is it a v5.0 agent or pre-v5.0 legacy? | Cannot assign it to registry without classification |
| U4 | @LanguageAgent identity | Appears as active HIGH PRIORITY task in AGENTS-CONFIG.md but is defined nowhere. Is it Language Polisher & Adapter (v5.0 LATER), or a separate agent? | Active task assigned to undefined agent |
| U5 | TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR | Fully defined in AGENTS-REGISTRY.md. Are they part of v5.0 or are they the generic predecessor? Do they remain active or are they replaced by pipeline agents? | Double entries in any registry if not resolved |
| U6 | BRIDGE role | Named in SYSTEM RULES v1.2 ("BRIDGE ei otsusta strateegiat" — BRIDGE does not decide strategy). No agent with this name or role exists in v5.0 pipeline. What is BRIDGE? | Unknown — could be an integration layer, a deprecated concept, or a missing agent |
| U7 | Children's section agent | ORCHESTRATOR-FLOW.md marks this as "Future work — no specific active agent assigned yet." No agent name. No v5.0 assignment. | Unregistered future need |
| U8 | Official agent IDs | v5.0 names use human-readable names (System Orchestrator, Offer Architect). Technical IDs use ALL-CAPS (GENESIS-ORCHESTRATOR, OFFER-ARCHITECT). Which format is the official ID format for v5.0? | Registry requires consistent ID format |
| U9 | Whether v5.0 supersedes AGENTS-REGISTRY.md | AGENTS-REGISTRY.md defines 4 technical agents with full specification. ORCHESTRATOR-FLOW.md defines 14 pipeline agents. Are these parallel systems or does v5.0 replace the technical agent layer? | Structural — affects registry architecture |

---

## SECTION 7 — REQUIRED HUMAN APPROVAL

The following items require explicit approval from Source before AGENT-REGISTRY.md can be created.

**Source must review this document and answer these questions:**

### 7.1 Agent Count
> What is the official total number of agents in MASTER SYSTEM STRUCTURE v5.0?
> (Current reconstruction shows 14 named agents. Confirm or correct.)

### 7.2 Layer Assignment
> Does a layer model (Layer 0 → Layer IX or similar) exist?
> If yes, assign each agent in Section 3 to its layer.
> If no, confirm that layers are not part of v5.0.

### 7.3 COURSE-CREATOR Status
> Is COURSE-CREATOR a v5.0 agent (to be assigned an official name and layer)?
> Or is it a pre-v5.0 legacy agent to be archived?

### 7.4 @LanguageAgent Identity
> Is @LanguageAgent the same as "Language Polisher & Adapter" (v5.0 LATER)?
> Or is it a separate, currently unregistered agent?
> The HIGH PRIORITY task assigned to @LanguageAgent in AGENTS-CONFIG.md requires resolution.

### 7.5 Technical Agents Status
> Do TASK-EXECUTOR, OUTPUT-VALIDATOR, and SYSTEM-AUDITOR remain active in v5.0?
> Or are they superseded by the pipeline agents (Humanizer, Brand Guardian, Integrity Auditor)?

### 7.6 BRIDGE Role
> What is the BRIDGE role referenced in SYSTEM RULES v1.2?
> Is it an agent, a concept, or a deprecated term?

### 7.7 ID Format
> What is the official agent ID format for v5.0?
> Option A: Human-readable (System Orchestrator, Offer Architect)
> Option B: ALL-CAPS (GENESIS-ORCHESTRATOR, OFFER-ARCHITECT)
> Option C: Both (human-readable display name + ALL-CAPS technical ID)

### 7.8 Authority Confirmation
> Once Source answers the above questions and confirms this document,
> explicitly state: "MASTER SYSTEM STRUCTURE v5.0-DRAFT is approved as the source for AGENT-REGISTRY.md"
> This statement is the unblock condition.

---

## SECTION 8 — NEXT STEP TO ENABLE AGENT-REGISTRY.md

The sequence to unblock registry creation:

```
Step 1 — Source reviews this DRAFT document
  └─ Answer all questions in Section 7
  └─ Correct any errors in Sections 3, 4, 5

Step 2 — Source approves this document
  └─ Explicit approval statement required (see Section 7.8)
  └─ Optional: rename file from DRAFT to APPROVED (remove DRAFT suffix)

Step 3 — Create AGENT-REGISTRY.md
  └─ Use this document as the sole source
  └─ Every agent entry must match an entry in Section 3 or 4 (after corrections)
  └─ Do not invent agents not present in this document
  └─ Do not create registry entries for unresolved items in Section 6

Step 4 — Remove AGENT-REGISTRY-BLOCKER-REPORT.md
  └─ Once registry is created and validated, the blocker report is obsolete
```

**Until Step 2 is complete: AGENT-REGISTRY.md will not be created.**

---

*This file was produced by source reconstruction only.*
*No agents were invented. No authority was fabricated. No IDs were guessed.*
*All evidence cited traces to specific files in this repository.*
