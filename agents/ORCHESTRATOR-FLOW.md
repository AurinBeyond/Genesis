# ORCHESTRATOR FLOW v2.0
# AurinBeyond / Genesis — Website Creation System
# Aligned to Master Structure v5.0
# Status: ACTIVE DESIGN
# Source approval required before any agent acts on this document.

---

## SECTION 1 — NAME ALIGNMENT FIXES

The following ad-hoc or unofficial agent names have been replaced with official Master Structure v5.0 names.

| Previous Name | Official v5.0 Name | Notes |
|---|---|---|
| GENESIS-ORCHESTRATOR | System Orchestrator | Same role, official name |
| OFFER-ARCHITECT | Offer Architect | Same role, official name |
| FUNNEL-ARCHITECT | Funnel Architect | Same role, official name |
| CONTENT-PRODUCER | Content Producer | Same role, official name |
| HUMANIZER | Humanizer | Unchanged — already official |
| BRAND-GUARDIAN | Brand Guardian | Same role, official name |
| PAGE-ARCHITECT | Genesis Architect | Site/page structure = Genesis Architect scope |
| COPY-AGENT | Content Producer | Consolidated under Content Producer |
| TRUST-LAYER-AGENT | Frequency Transmitter | Authority/about content = frequency transmission |
| LEGAL-AGENT | Legal & Compliance Guard | Same role, official name |
| COMMUNITY-AGENT | Community Catalyst | Same role, official name |
| CHILDREN-SECTION-AGENT | (future work) | Marked LATER — no active assignment yet |
| SEWING-COURSE-AGENT | NOT USED | External / separate brand — removed from registry |

Agents present in Master Structure v5.0 but not yet active in this pipeline:
- **Visual Director** — LATER (design/visual production phase)
- **Language Polisher & Adapter** — LATER (localization/adaptation phase)
- **Integrity Auditor** — LATER (full audit phase post-launch)
- **Product Delivery System** — LATER (delivery infrastructure phase)

---

## SECTION 2 — UPDATED ACTIVE AGENTS

### System Orchestrator
- **Official ID:** System Orchestrator
- **Role:** Reads TASKMASTER.md, assigns tasks, enforces sequence, triggers handoffs
- **Input:** TASKMASTER.md, logs/updates.log
- **Output:** Task assignment to next agent
- **Trigger:** Source adds task with status `pending`
- **Stop condition:** Task status is `review` — waits for Source approval
- **Status:** ACTIVE NOW

---

### Offer Architect
- **Official ID:** Offer Architect
- **Role:** Defines products: name, transformation, format, price, audience
- **Input:** Source brief or Genesis content (01-the-source-within.md etc.)
- **Output:** Offer definition doc (logs/outputs/TASK-XXX/01-offer.md)
- **Trigger:** Source task with offer creation intent
- **Stop condition:** Output in REVIEW — waits for Source
- **Status:** ACTIVE NOW — Step 1 of pipeline

---

### Funnel Architect
- **Official ID:** Funnel Architect
- **Role:** Defines the sales flow for each offer: entry point, headline, problem statement, shift, offer, CTA
- **Input:** Approved 01-offer.md from Offer Architect
- **Output:** logs/outputs/TASK-XXX/02-funnel.md
- **Trigger:** Source approves Step 1 output
- **Stop condition:** Funnel draft written — status REVIEW
- **Status:** ACTIVE NOW — Step 2 of pipeline

---

### Content Producer
- **Official ID:** Content Producer
- **Role:** Writes raw section copy based on approved funnel structure or page architecture
- **Input:** Approved 02-funnel.md from Funnel Architect, or page structure doc from Genesis Architect
- **Output:** logs/outputs/TASK-XXX/03-content.md
- **Trigger:** Source approves Step 2 output
- **Stop condition:** Raw copy written — status REVIEW
- **Status:** ACTIVE NOW — Step 3 of pipeline

---

### Humanizer
- **Official ID:** Humanizer
- **Role:** Transforms raw agent output into brand-consistent, human-voice copy. Removes AI patterns.
- **Input:** Content Producer output (approved Step 3)
- **Output:** logs/outputs/TASK-XXX/04-humanized.md
- **Trigger:** Source approves Step 3 output
- **Stop condition:** Output saved — task moves to REVIEW
- **Status:** ACTIVE NOW — Step 4 of pipeline — mandatory, no exceptions

---

### Brand Guardian
- **Official ID:** Brand Guardian
- **Role:** Validates all content against brand identity (tone, values, visual rules from SYSTEM_RULES.md). Assembles FINAL.md.
- **Input:** All approved step outputs for a task
- **Output:** Approved or rejected draft with notes; FINAL.md on approval
- **Trigger:** Source approves Step 4 output
- **Stop condition:** FINAL.md assembled — status REVIEW
- **Status:** ACTIVE NOW — Step 5 of pipeline — mandatory, no exceptions

---

### Genesis Architect
- **Official ID:** Genesis Architect
- **Role:** Defines page structure (sections, hierarchy, flow) for each site page. No copy. No code.
- **Input:** Offer definition or content brief
- **Output:** Page structure doc (section list + purpose per section)
- **Trigger:** Offer or book/course definition approved by Source
- **Stop condition:** Structure doc complete — passes to Content Producer
- **Status:** ACTIVE NOW — runs as standalone task for site pages

---

### Frequency Transmitter
- **Official ID:** Frequency Transmitter
- **Role:** Builds authority content: about, proof, credentials, testimony structure — transmits the Genesis signal
- **Input:** Brand identity + offer definitions
- **Output:** Trust and authority section drafts
- **Trigger:** Core offers defined and approved
- **Stop condition:** Drafts in REVIEW
- **Status:** ACTIVE NOW — runs as its own task

---

### Legal & Compliance Guard
- **Official ID:** Legal & Compliance Guard
- **Role:** Produces legal pages: Terms, Privacy, Disclaimer — based on offer type and jurisdiction
- **Input:** Offer definitions, site scope
- **Output:** Legal page drafts
- **Trigger:** Offer ecosystem defined
- **Stop condition:** Legal drafts in REVIEW
- **Status:** ACTIVE NOW — runs as its own task

---

### Community Catalyst
- **Official ID:** Community Catalyst
- **Role:** Designs community/contact touchpoints: newsletter, community page, contact flow
- **Input:** Offer ecosystem + authority layer
- **Output:** Community section drafts
- **Trigger:** Core site complete
- **Stop condition:** Drafts in REVIEW
- **Status:** LATER — after core site is live

---

### Children's Section Work
- **Official classification:** Future work — no specific active agent assigned yet
- **Role:** Age-appropriate content aligned with core values
- **Status:** LATER — after core site is live. Will be assigned an agent from Master Structure v5.0 at that time.

---

### Visual Director
- **Official ID:** Visual Director
- **Status:** LATER — design/visual production phase

---

### Language Polisher & Adapter
- **Official ID:** Language Polisher & Adapter
- **Status:** LATER — localization and adaptation phase

---

### Integrity Auditor
- **Official ID:** Integrity Auditor
- **Status:** LATER — full system audit phase post-launch

---

### Product Delivery System
- **Official ID:** Product Delivery System
- **Status:** LATER — delivery infrastructure phase

---

## SECTION 3 — UPDATED FLOW

Strict sequence. One task active at a time. Each task runs through a 5-step pipeline.

```
Source
  └─ adds task to TASKMASTER.md (status: pending)
       │
       ▼
System Orchestrator
  └─ reads task, assigns to STEP 1 agent
  └─ writes: TASKMASTER current_step = 1, next_agent = Offer Architect
       │
       ▼
STEP 1 — Offer Architect
  └─ defines product / offer
  └─ writes: logs/outputs/TASK-XXX/01-offer.md
  └─ logs: TASK-XXX → STEP 1: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 2 — Funnel Architect
  └─ defines sales flow for the offer
  └─ writes: logs/outputs/TASK-XXX/02-funnel.md
  └─ logs: TASK-XXX → STEP 2: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 3 — Content Producer
  └─ writes raw section copy based on funnel structure
  └─ writes: logs/outputs/TASK-XXX/03-content.md
  └─ logs: TASK-XXX → STEP 3: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 4 — Humanizer
  └─ rewrites in brand-consistent human voice
  └─ writes: logs/outputs/TASK-XXX/04-humanized.md
  └─ logs: TASK-XXX → STEP 4: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 5 — Brand Guardian
  └─ validates all steps against brand identity
  └─ assembles FINAL.md from approved steps
  └─ writes: logs/outputs/TASK-XXX/FINAL.md
  └─ logs: TASK-XXX → STEP 5: FINAL assembled
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
Source → moves task to COMPLETED TASKS in TASKMASTER.md
```

**Handoff table:**

| Step | Input Source | Output File | Next Agent | Validation Condition |
|---|---|---|---|---|
| 0 | Source (TASKMASTER.md) | — | System Orchestrator | Task status = pending |
| 1 | Orchestrator assignment | TASK-XXX/01-offer.md | Funnel Architect | Source approves Step 1 |
| 2 | 01-offer.md approved | TASK-XXX/02-funnel.md | Content Producer | Source approves Step 2 |
| 3 | 02-funnel.md approved | TASK-XXX/03-content.md | Humanizer | Source approves Step 3 |
| 4 | 03-content.md approved | TASK-XXX/04-humanized.md | Brand Guardian | Source approves Step 4 |
| 5 | 04-humanized.md approved | TASK-XXX/FINAL.md | Source (release) | Brand Guardian sign-off |

---

## SECTION 4 — ROLE MAPPING CHECK

Minimum active agents required to build the website now:

| Agent (v5.0) | Pipeline Role | Task Type |
|---|---|---|
| System Orchestrator | Task routing and step tracking | System |
| Offer Architect | Step 1: product/offer definition | Pipeline |
| Funnel Architect | Step 2: sales flow definition | Pipeline |
| Content Producer | Step 3: raw copy per section | Pipeline |
| Humanizer | Step 4: brand-voice rewrite (mandatory) | Pipeline |
| Brand Guardian | Step 5: validation + FINAL assembly (mandatory) | Pipeline |
| Genesis Architect | Page structure for site pages | Standalone task |
| Frequency Transmitter | Authority/about content | Standalone task |
| Legal & Compliance Guard | Legal pages | Standalone task |

Total active now: 9 agents.

Agents confirmed in Master Structure v5.0 but not yet active:

| Agent (v5.0) | Planned Phase |
|---|---|
| Visual Director | Design/visual production |
| Language Polisher & Adapter | Localization/adaptation |
| Integrity Auditor | Post-launch audit |
| Product Delivery System | Delivery infrastructure |
| Community Catalyst | After core site is live |
| Children's section work | After core site is live |

---

## SECTION 5 — VALIDATION

### Name alignment: COMPLETE
All unofficial agent names replaced with Master Structure v5.0 names. No ad-hoc IDs remain in the active flow.

### Role coverage: COMPLETE
Every step in the 5-step pipeline maps to an official v5.0 agent. Standalone tasks (site pages, trust layer, legal) map to official agents.

### Gaps noted: NONE for current phase
Future agents are documented and marked LATER. Children's section is preserved in the system — marked LATER, not excluded.

### Source approval logic: PRESERVED
Every step pauses at REVIEW. Source approval required before the next step starts. No agent marks a task DONE.

### Handoff logic: PRESERVED
Pipeline sequence unchanged: Offer Architect → Funnel Architect → Content Producer → Humanizer → Brand Guardian. Only agent labels updated.

### Control rules: PRESERVED (see below)

---

## CONTROL RULES

1. **No overwriting outputs.** Agent must check if its step file exists before writing. If it exists — STOP, log conflict, notify Source.
2. **Strict sequence.** Steps run in order: 1 → 2 → 3 → 4 → 5. No skipping.
3. **No agent writes to a future step.** Offer Architect writes only 01-offer.md. Funnel Architect writes only 02-funnel.md. Etc.
4. **Humanizer mandatory.** Step 4 runs on every task. No exceptions.
5. **Brand Guardian mandatory.** Step 5 runs on every task and assembles FINAL.md.
6. **Source approval required between each step.** Execution pauses after every step. Source decides before the next step starts.
7. **System Orchestrator only assigns one step at a time.** No parallel execution.
8. **No agent marks a task DONE.** Only Source can set status = done.
9. **Output moves forward only.** A completed step is not re-executed unless Source explicitly resets it.

---

## OFFER ECOSYSTEM

### Entry Product
- Low-cost digital product (€17–€27)
- Format: PDF protocol / workbook
- Purpose: First transaction, trust establishment
- Example: The Silent Reset (TASK-001 output)

### Books
- Long-form written works aligned with Genesis content
- Format: PDF / Kindle / print
- Price range: €12–€25
- Content source: 01–07 Genesis chapters

### Courses
- Structured multi-module learning
- Format: video + workbook or text-only protocol
- Price range: €97–€297
- Topic: Internal authority, perception, identity, system detachment

### Children's Section
- Age-appropriate content aligned with core values
- Format: illustrated PDF / simple interactive content
- Status: LATER — after core site is live

### Community
- Newsletter or private community
- Purpose: Ongoing relationship, trust deepening
- Format: Email list + optional paid membership
- Status: LATER

### Trust Layer
- About page, proof of concept, methodology explanation
- Not testimonial-heavy — authority through clarity
- Mandatory before any paid offer goes live
- Agent: Frequency Transmitter

---

## LAUNCH REQUIREMENTS

The following must exist before the site goes live:

### Content
- [ ] Homepage / Gateway — structure + copy approved
- [ ] At least one entry product defined and approved (TASK-001 complete)
- [ ] About / Trust layer page — drafted and approved
- [ ] One book or course page — structure + copy approved

### Legal
- [ ] Terms of Service — drafted and approved
- [ ] Privacy Policy — drafted and approved
- [ ] Disclaimer — drafted and approved

### Technical
- [ ] All pages render correctly on mobile (below 600px)
- [ ] Site flow follows: index → void → core → delta-insight → sigma-core → sigma-protocol
- [ ] No external frameworks used
- [ ] All CSS consolidated into assets/css/style.css

### System
- [ ] TASKMASTER.md reflects current state
- [ ] logs/updates.log has full execution history
- [ ] All outputs in logs/outputs/ are Source-approved before publishing

### Brand
- [ ] Brand Guardian has reviewed all live pages
- [ ] Humanizer pass completed on all final copy
- [ ] Visual identity matches SYSTEM_RULES.md spec (black #050505, gold #d4af37, Inter font)

---

**Control remains with the Source. No step executes without a task. No output publishes without approval.**
