# MASTER SYSTEM STRUCTURE v5.0
# AurinBeyond / Genesis
# Status: FINAL — AUTHORITATIVE SOURCE
# Date: 2026-04-07

---

## AUTHORITY STATEMENT

This document is the sole authoritative source for all agent definitions in the system.

All prior drafts, reconstruction files, and scattered agent references are superseded by this document.

---

## CONTROL RULE

If an agent is not defined here, it does not exist.

No agent may be invoked, registered, or referenced unless it appears in the OFFICIAL AGENT LIST below.

---

## REGISTRY ENABLEMENT

AGENT-REGISTRY.md creation is now unblocked.

Source: this document.
Condition: met.

---

## OFFICIAL AGENT LIST

**Total official agents: 15**

### Phase 1 — Active Now (10 agents)

| # | Official v5.0 Name | Technical ID | Layer |
|---|---|---|---|
| 1 | System Orchestrator | GENESIS-ORCHESTRATOR | II |
| 2 | Offer Architect | OFFER-ARCHITECT | IV |
| 3 | Funnel Architect | FUNNEL-ARCHITECT | IV |
| 4 | Content Producer | CONTENT-PRODUCER | IV |
| 5 | Humanizer | HUMANIZER | IV |
| 6 | Brand Guardian | BRAND-GUARDIAN | IV |
| 7 | Genesis Architect | GENESIS-ARCHITECT | V |
| 8 | Frequency Transmitter | FREQUENCY-TRANSMITTER | V |
| 9 | Legal & Compliance Guard | LEGAL-GUARD | V |
| 10 | Course Creator | COURSE-CREATOR | VI |

### Phase 2 — Later (5 agents)

| # | Official v5.0 Name | Technical ID | Layer | Activation Phase |
|---|---|---|---|---|
| 11 | Community Catalyst | COMMUNITY-CATALYST | VII | After core site is live |
| 12 | Visual Director | VISUAL-DIRECTOR | IX | Design/visual production phase |
| 13 | Language Polisher & Adapter | LANGUAGE-POLISHER | VIII | Localization/adaptation phase |
| 14 | Integrity Auditor | INTEGRITY-AUDITOR | VIII | Full system audit post-launch |
| 15 | Product Delivery System | PRODUCT-DELIVERY | IX | Delivery infrastructure phase |

**FINAL AGENT COUNT: 15**

No additional agents exist. No aliases appear in this list.

---

## FINAL LAYER MODEL

Layer numbers are locked. Agent assignments are final.

```
LAYER 0 — CORE SYSTEM
  Files: core/GENESIS-LAWS.md, core/STATE.md, core/MODE.md, core/INPUT.md, core/OUTPUT-STANDARD.md
  Agents: none — rule layer, not execution layer
  Purpose: Defines laws, state values, input/output standards

LAYER I — OPERATIONAL LAWS
  Files: laws/GENESIS-OPERATION.md
  Agents: none — execution rules layer
  Purpose: Defines how agents execute, escalate, and hand off

LAYER II — ORCHESTRATION
  Agents: System Orchestrator (GENESIS-ORCHESTRATOR)
  Purpose: Reads TASKMASTER.md; assigns tasks; enforces pipeline sequence; triggers handoffs

LAYER III — TECHNICAL / SYSTEM ROLES
  Roles: TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR
  Purpose: Infrastructure execution, output validation, system integrity
  Note: These are system roles, not official v5.0 content agents.
        They operate below the content pipeline. See TECHNICAL/SYSTEM ROLES section.

LAYER IV — CONTENT PIPELINE (Active Now)
  Agents: Offer Architect (Step 1), Funnel Architect (Step 2),
          Content Producer (Step 3), Humanizer (Step 4 — MANDATORY),
          Brand Guardian (Step 5 — MANDATORY)
  Purpose: 5-step sequential content production pipeline

LAYER V — ARCHITECTURE & AUTHORITY AGENTS (Active Now)
  Agents: Genesis Architect, Frequency Transmitter, Legal & Compliance Guard
  Purpose: Standalone task execution — page structure, authority content, legal pages

LAYER VI — SPECIALIZED CONTENT AGENTS (Active Now)
  Agents: Course Creator
  Purpose: Course and educational content production

LAYER VII — COMMUNITY & GROWTH AGENTS (Later)
  Agents: Community Catalyst
  Purpose: Community engagement, newsletter, contact flow

LAYER VIII — QUALITY & LOCALIZATION AGENTS (Later)
  Agents: Language Polisher & Adapter, Integrity Auditor
  Purpose: Localization, full system audit post-launch

LAYER IX — VISUAL & DELIVERY AGENTS (Later)
  Agents: Visual Director, Product Delivery System
  Purpose: Visual production, delivery infrastructure
```

---

## AGENT ID FORMAT

Official format: **Human-readable display name + ALL-CAPS technical ID**

- Display name used in documentation, instructions, and task routing (e.g., `System Orchestrator`)
- Technical ID used in registry entries, config files, and system references (e.g., `GENESIS-ORCHESTRATOR`)
- Both refer to the same agent. Neither is an alias for a different agent.

---

## OFFICIAL AGENT DEFINITIONS

### LAYER II — ORCHESTRATION

---

**System Orchestrator**
- Technical ID: `GENESIS-ORCHESTRATOR`
- Layer: II
- Role: Reads TASKMASTER.md; assigns tasks to pipeline agents; enforces step sequence; triggers handoffs
- Activation trigger: Source adds task to TASKMASTER.md with status `pending`
- Stop condition: Task status is `review` — waits for Source approval
- Mandatory: Yes — every task passes through this agent
- Controls: All Layer IV, V, VI agents

---

### LAYER IV — CONTENT PIPELINE

---

**Offer Architect**
- Technical ID: `OFFER-ARCHITECT`
- Layer: IV — Pipeline Step 1
- Role: Defines products — name, transformation, format, price, audience
- Activation trigger: System Orchestrator assigns Step 1
- Stop condition: Output written to `logs/outputs/TASK-XXX/01-offer.md`, status set to REVIEW
- Input: Task brief from TASKMASTER.md
- Output: `01-offer.md`

---

**Funnel Architect**
- Technical ID: `FUNNEL-ARCHITECT`
- Layer: IV — Pipeline Step 2
- Role: Defines sales flow — entry point, headline, problem statement, shift, offer, CTA
- Activation trigger: Source approves `01-offer.md`
- Stop condition: Output written to `logs/outputs/TASK-XXX/02-funnel.md`, status set to REVIEW
- Input: Approved `01-offer.md`
- Output: `02-funnel.md`

---

**Content Producer**
- Technical ID: `CONTENT-PRODUCER`
- Layer: IV — Pipeline Step 3
- Role: Writes raw section copy based on approved funnel structure or page architecture
- Activation trigger: Source approves `02-funnel.md` (or page structure from Genesis Architect)
- Stop condition: Output written to `logs/outputs/TASK-XXX/03-content.md`, status set to REVIEW
- Input: Approved `02-funnel.md` or Genesis Architect structure doc
- Output: `03-content.md`

---

**Humanizer**
- Technical ID: `HUMANIZER`
- Layer: IV — Pipeline Step 4
- Role: Transforms raw agent output into brand-consistent, human-voice copy; removes AI patterns
- Activation trigger: Source approves `03-content.md`
- Stop condition: Output written to `logs/outputs/TASK-XXX/04-humanized.md`, status set to REVIEW
- Input: Approved `03-content.md`
- Output: `04-humanized.md`
- **MANDATORY — no exceptions. Every task passes through this step.**

---

**Brand Guardian**
- Technical ID: `BRAND-GUARDIAN`
- Layer: IV — Pipeline Step 5
- Role: Validates all content against brand identity (tone, values, visual rules); assembles FINAL.md
- Activation trigger: Source approves `04-humanized.md`
- Stop condition: `FINAL.md` assembled, status set to REVIEW
- Input: All approved step outputs for the task
- Output: `FINAL.md`
- **MANDATORY — no exceptions. Final gate before Source release decision.**

---

### LAYER V — ARCHITECTURE & AUTHORITY

---

**Genesis Architect**
- Technical ID: `GENESIS-ARCHITECT`
- Layer: V
- Role: Defines page structure (sections, hierarchy, flow) for each site page — no copy, no code
- Activation trigger: Offer or book/course definition approved by Source
- Stop condition: Structure doc complete; passed to Content Producer
- Input: Approved offer or product definition
- Output: Page structure document → feeds Content Producer

---

**Frequency Transmitter**
- Technical ID: `FREQUENCY-TRANSMITTER`
- Layer: V
- Role: Builds authority content — about page, proof, credentials, testimony structure; transmits the Genesis signal
- Activation trigger: Core offers defined and approved by Source
- Stop condition: Authority content drafts in REVIEW
- Input: Approved core offer definitions
- Output: Authority/trust layer content drafts

---

**Legal & Compliance Guard**
- Technical ID: `LEGAL-GUARD`
- Layer: V
- Role: Produces legal pages — Terms, Privacy, Disclaimer — based on offer type and jurisdiction
- Activation trigger: Offer ecosystem defined by Source
- Stop condition: Legal drafts in REVIEW
- Input: Offer type, jurisdiction parameters
- Output: Legal page drafts
- Note: No dependency on content pipeline; standalone task

---

### LAYER VI — SPECIALIZED CONTENT

---

**Course Creator**
- Technical ID: `COURSE-CREATOR`
- Layer: VI
- Role: Produces course and educational content structure, curriculum outline, and delivery materials
- Activation trigger: Source assigns course production task
- Stop condition: Course materials in REVIEW
- Definition file: `agents/course-creator/agent.md` (v1.1)
- Note: Standalone agent; operates independently from 5-step pipeline

---

### LAYER VII — COMMUNITY & GROWTH (Later)

---

**Community Catalyst**
- Technical ID: `COMMUNITY-CATALYST`
- Layer: VII
- Role: Community engagement, newsletter, contact flow management
- Activation phase: After core site is live
- Status: LATER — not active in Phase 1

---

### LAYER VIII — QUALITY & LOCALIZATION (Later)

---

**Language Polisher & Adapter**
- Technical ID: `LANGUAGE-POLISHER`
- Layer: VIII
- Role: Localization and language adaptation of approved content
- Activation phase: Localization/adaptation phase
- Status: LATER — not active in Phase 1
- Note: References to `@LanguageAgent` in task configs resolve to this agent

---

**Integrity Auditor**
- Technical ID: `INTEGRITY-AUDITOR`
- Layer: VIII
- Role: Full system audit post-launch; checks integrity of all agent outputs and registry alignment
- Activation phase: Full system audit post-launch
- Status: LATER — not active in Phase 1

---

### LAYER IX — VISUAL & DELIVERY (Later)

---

**Visual Director**
- Technical ID: `VISUAL-DIRECTOR`
- Layer: IX
- Role: Visual production and design direction
- Activation phase: Design/visual production phase
- Status: LATER — not active in Phase 1

---

**Product Delivery System**
- Technical ID: `PRODUCT-DELIVERY`
- Layer: IX
- Role: Delivery infrastructure for digital products
- Activation phase: Delivery infrastructure phase
- Status: LATER — not active in Phase 1

---

## TECHNICAL / SYSTEM ROLES

These roles exist at Layer III. They are infrastructure-level roles, not content pipeline agents.
They are NOT part of the official agent count (15). They do not produce content output.

| Technical ID | Role | Status |
|---|---|---|
| `TASK-EXECUTOR` | Executes defined tasks at the system level | Active — infrastructure layer |
| `OUTPUT-VALIDATOR` | Validates outputs at the system level | Active — infrastructure layer |
| `SYSTEM-AUDITOR` | Ensures system integrity | Active — infrastructure layer; distinct from Integrity Auditor (Layer VIII content audit) |

---

## LEGACY / ALIAS NAME MAP

All historical and unofficial names resolved to their official v5.0 designations.

| Legacy / Unofficial Name | Official v5.0 Name | Technical ID | Notes |
|---|---|---|---|
| GENESIS-ORCHESTRATOR | System Orchestrator | GENESIS-ORCHESTRATOR | Technical ID retained |
| OFFER-ARCHITECT | Offer Architect | OFFER-ARCHITECT | Technical ID retained |
| FUNNEL-ARCHITECT | Funnel Architect | FUNNEL-ARCHITECT | Technical ID retained |
| CONTENT-PRODUCER | Content Producer | CONTENT-PRODUCER | Technical ID retained |
| COPY-AGENT | Content Producer | CONTENT-PRODUCER | Consolidated under Content Producer |
| HUMANIZER | Humanizer | HUMANIZER | Unchanged — already official |
| BRAND-GUARDIAN | Brand Guardian | BRAND-GUARDIAN | Technical ID retained |
| PAGE-ARCHITECT | Genesis Architect | GENESIS-ARCHITECT | Site/page structure = Genesis Architect scope |
| TRUST-LAYER-AGENT | Frequency Transmitter | FREQUENCY-TRANSMITTER | Authority/about content = frequency transmission |
| LEGAL-AGENT | Legal & Compliance Guard | LEGAL-GUARD | Renamed for clarity |
| COMMUNITY-AGENT | Community Catalyst | COMMUNITY-CATALYST | Renamed |
| COURSE-CREATOR | Course Creator | COURSE-CREATOR | Technical ID retained; now official v5.0 |
| @LanguageAgent | Language Polisher & Adapter | LANGUAGE-POLISHER | Task-config handle resolves to this agent |
| SEWING-COURSE-AGENT | NOT USED — removed | — | External / separate brand — removed from system |
| CHILDREN-SECTION-AGENT | NOT USED — not yet assigned | — | Future work; no agent assigned; not in registry |
| BRIDGE | NOT AN AGENT — system concept | — | Named in SYSTEM RULES v1.2; no agent counterpart; refers to inter-layer communication, not an agent |

---

## SYSTEM PIPELINE FLOW

```
SOURCE (AurinBeyond)
  └─ adds task to TASKMASTER.md (status: pending)
       │
       ▼
System Orchestrator (GENESIS-ORCHESTRATOR)
  └─ reads task from TASKMASTER.md
  └─ assigns to Step 1 agent
  └─ enforces sequence
  └─ triggers handoffs
       │
       ▼
CONTENT PIPELINE — 5-step sequential

  STEP 1 — Offer Architect
       └─ output: logs/outputs/TASK-XXX/01-offer.md → status: REVIEW
       └─ [Source approves]

  STEP 2 — Funnel Architect
       └─ input: approved 01-offer.md
       └─ output: logs/outputs/TASK-XXX/02-funnel.md → status: REVIEW
       └─ [Source approves]

  STEP 3 — Content Producer
       └─ input: approved 02-funnel.md (or page structure from Genesis Architect)
       └─ output: logs/outputs/TASK-XXX/03-content.md → status: REVIEW
       └─ [Source approves]

  STEP 4 — Humanizer  [MANDATORY — no exceptions]
       └─ input: approved 03-content.md
       └─ output: logs/outputs/TASK-XXX/04-humanized.md → status: REVIEW
       └─ [Source approves]

  STEP 5 — Brand Guardian  [MANDATORY — no exceptions]
       └─ input: all approved step outputs for this task
       └─ output: logs/outputs/TASK-XXX/FINAL.md → status: REVIEW
       └─ [Source approves → task moves to COMPLETED]
            │
            ▼
         OUTPUT: FINAL.md (approved and logged)
```

### Standalone Task Agents (outside the 5-step pipeline):

```
Source-approved trigger
  │
  ├─ Genesis Architect
  │    └─ Defines page structure → passes to Content Producer
  │
  ├─ Frequency Transmitter
  │    └─ Produces authority / trust layer content
  │
  ├─ Legal & Compliance Guard
  │    └─ Produces legal pages
  │
  └─ Course Creator
       └─ Produces course and educational content
```

---

## SYSTEM CONTROL RULES

- Only Source sets task status to DONE
- No agent marks a task DONE
- No agent skips steps
- No agent overwrites an existing step file
- System Orchestrator assigns one step at a time — no parallel execution
- Output moves forward only — no step re-executed unless Source explicitly resets it
- Source approval required between every pipeline step
- No agent invokes another agent not defined in this document

---

*This document is the final authority for AurinBeyond / Genesis agent system v5.0.*
*Approved: 2026-04-07*
*Supersedes: core/MASTER-SYSTEM-STRUCTURE-v5.0-DRAFT.md and all prior agent reference files.*
