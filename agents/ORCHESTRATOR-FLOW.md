# ORCHESTRATOR FLOW v1.0
# AurinBeyond / Genesis — Website Creation System
# Status: ACTIVE DESIGN
# Source approval required before any agent acts on this document.

---

## SECTION 1 — AGENT REGISTRY

### ORCHESTRATOR
- **ID:** GENESIS-ORCHESTRATOR
- **Role:** Reads TASKMASTER.md, assigns tasks, enforces sequence, triggers handoffs
- **Input:** TASKMASTER.md, logs/updates.log
- **Output:** Task assignment to next agent
- **Trigger:** Source adds task with status `pending`
- **Stop condition:** Task status is `review` — waits for Source approval
- **Status:** ACTIVE NOW

---

### BRAND-GUARDIAN
- **ID:** BRAND-GUARDIAN
- **Role:** Validates all content against brand identity (tone, values, visual rules from SYSTEM_RULES.md)
- **Input:** Draft output from any content agent
- **Output:** Approved or rejected draft with notes
- **Trigger:** Any content agent completes a draft
- **Stop condition:** Approved — passes to HUMANIZER
- **Status:** ACTIVE NOW

---

### HUMANIZER
- **ID:** HUMANIZER
- **Role:** Transforms raw agent output into brand-consistent, human-voice copy. Removes AI patterns.
- **Input:** BRAND-GUARDIAN approved draft
- **Output:** Final human-voice text, saved to logs/outputs/TASK-XXX.md
- **Trigger:** BRAND-GUARDIAN approval received
- **Stop condition:** Output saved — task moves to REVIEW
- **Status:** ACTIVE NOW — mandatory before any final output

---

### PAGE-ARCHITECT
- **ID:** PAGE-ARCHITECT
- **Role:** Defines page structure (sections, hierarchy, flow) for each site page. No copy. No code.
- **Input:** Offer definition or content brief
- **Output:** Page structure doc (section list + purpose per section)
- **Trigger:** Offer or book/course definition approved by Source
- **Stop condition:** Structure doc complete — passes to COPY-AGENT
- **Status:** ACTIVE NOW

---

### COPY-AGENT
- **ID:** COPY-AGENT
- **Role:** Writes raw section copy based on PAGE-ARCHITECT structure
- **Input:** Page structure doc + brand voice rules
- **Output:** Raw draft copy per section
- **Trigger:** PAGE-ARCHITECT output approved
- **Stop condition:** Draft complete — passes to BRAND-GUARDIAN
- **Status:** ACTIVE NOW

---

### OFFER-ARCHITECT
- **ID:** OFFER-ARCHITECT
- **Role:** Defines products: name, transformation, format, price, audience
- **Input:** Source brief or Genesis content (01-the-source-within.md etc.)
- **Output:** Offer definition doc (logs/outputs/TASK-XXX.md)
- **Trigger:** Source task with offer creation intent
- **Stop condition:** Output in REVIEW — waits for Source
- **Status:** ACTIVE NOW

---

### TRUST-LAYER-AGENT
- **ID:** TRUST-LAYER-AGENT
- **Role:** Builds authority content: about, proof, credentials, testimonial structure
- **Input:** Brand identity + offer definitions
- **Output:** Trust section drafts
- **Trigger:** Core offers defined and approved
- **Stop condition:** Trust drafts in REVIEW
- **Status:** ACTIVE NOW

---

### LEGAL-AGENT
- **ID:** LEGAL-AGENT
- **Role:** Produces legal pages: Terms, Privacy, Disclaimer — based on offer type and jurisdiction
- **Input:** Offer definitions, site scope
- **Output:** Legal page drafts
- **Trigger:** Offer ecosystem defined
- **Stop condition:** Legal drafts in REVIEW
- **Status:** ACTIVE NOW

---

### CHILDREN-SECTION-AGENT
- **ID:** CHILDREN-SECTION-AGENT
- **Role:** Creates content for the children's area of the site (age-appropriate, brand-consistent)
- **Input:** Source brief + brand rules
- **Output:** Section drafts for children's area
- **Trigger:** Core site sections complete
- **Stop condition:** Drafts in REVIEW
- **Status:** LATER — after core site is live

---

### COMMUNITY-AGENT
- **ID:** COMMUNITY-AGENT
- **Role:** Designs community/contact touchpoints: newsletter, community page, contact flow
- **Input:** Offer ecosystem + trust layer
- **Output:** Community section drafts
- **Trigger:** Core site complete
- **Stop condition:** Drafts in REVIEW
- **Status:** LATER

---

### FUNNEL-ARCHITECT
- **ID:** FUNNEL-ARCHITECT
- **Role:** Defines the sales flow for each offer: entry point, headline, problem statement, shift, offer, CTA
- **Input:** Approved 01-offer.md from OFFER-ARCHITECT
- **Output:** logs/outputs/TASK-XXX/02-funnel.md
- **Trigger:** Source approves Step 1 output
- **Stop condition:** Funnel draft written — status REVIEW
- **Status:** ACTIVE NOW

---

### CONTENT-PRODUCER
- **ID:** CONTENT-PRODUCER
- **Role:** Writes raw section copy based on approved funnel structure
- **Input:** Approved 02-funnel.md from FUNNEL-ARCHITECT
- **Output:** logs/outputs/TASK-XXX/03-content.md
- **Trigger:** Source approves Step 2 output
- **Stop condition:** Raw copy written — status REVIEW
- **Status:** ACTIVE NOW

---

### SEWING-COURSE-AGENT
- **ID:** SEWING-COURSE-AGENT
- **Role:** External brand. Not part of this system.
- **Status:** NOT USED — external / future / separate brand

---

## SECTION 2 — ORCHESTRATOR FLOW

Strict sequence. One task active at a time. Each task runs through a 5-step pipeline.

```
Source
  └─ adds task to TASKMASTER.md (status: pending)
       │
       ▼
GENESIS-ORCHESTRATOR
  └─ reads task, assigns to STEP 1 agent
  └─ writes: TASKMASTER current_step = 1, next_agent = OFFER-ARCHITECT
       │
       ▼
STEP 1 — OFFER-ARCHITECT
  └─ defines product / offer
  └─ writes: logs/outputs/TASK-XXX/01-offer.md
  └─ logs: TASK-XXX → STEP 1: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 2 — FUNNEL-ARCHITECT
  └─ defines sales flow for the offer
  └─ writes: logs/outputs/TASK-XXX/02-funnel.md
  └─ logs: TASK-XXX → STEP 2: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 3 — CONTENT-PRODUCER
  └─ writes raw section copy based on funnel structure
  └─ writes: logs/outputs/TASK-XXX/03-content.md
  └─ logs: TASK-XXX → STEP 3: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 4 — HUMANIZER
  └─ rewrites in brand-consistent human voice
  └─ writes: logs/outputs/TASK-XXX/04-humanized.md
  └─ logs: TASK-XXX → STEP 4: output generated
  └─ sets status: REVIEW
       │
       ▼ Source approves
       │
STEP 5 — BRAND-GUARDIAN
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

---

## SECTION 3 — HANDOFF LOGIC

| Step | Input Source | Output File | Next Agent | Validation Condition |
|---|---|---|---|---|
| 0 | Source (TASKMASTER.md) | — | GENESIS-ORCHESTRATOR | Task status = pending |
| 1 | ORCHESTRATOR assignment | TASK-XXX/01-offer.md | FUNNEL-ARCHITECT | Source approves Step 1 |
| 2 | 01-offer.md approved | TASK-XXX/02-funnel.md | CONTENT-PRODUCER | Source approves Step 2 |
| 3 | 02-funnel.md approved | TASK-XXX/03-content.md | HUMANIZER | Source approves Step 3 |
| 4 | 03-content.md approved | TASK-XXX/04-humanized.md | BRAND-GUARDIAN | Source approves Step 4 |
| 5 | 04-humanized.md approved | TASK-XXX/FINAL.md | Source (release) | Brand Guardian sign-off |

---

## SECTION 4 — MINIMUM ACTIVE AGENTS

Required to build the website now (full 5-step pipeline):

1. **GENESIS-ORCHESTRATOR** — task routing and step tracking
2. **OFFER-ARCHITECT** — Step 1: product/offer definition
3. **FUNNEL-ARCHITECT** — Step 2: sales flow definition
4. **CONTENT-PRODUCER** — Step 3: raw copy per section
5. **HUMANIZER** — Step 4: brand-voice rewrite (mandatory)
6. **BRAND-GUARDIAN** — Step 5: validation + FINAL assembly (mandatory)
7. **TRUST-LAYER-AGENT** — authority/about content (runs as its own task)
8. **LEGAL-AGENT** — legal pages (runs as its own task)

Total: 8 agents. No extras.

---

## SECTION 5 — OFFER ECOSYSTEM

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

### Sewing Course
- **EXTERNAL / FUTURE / SEPARATE BRAND**
- Not part of AurinBeyond / Genesis ecosystem
- Do not include in site structure or agent tasks

---

## SECTION 6 — CONTROL RULES

1. **No overwriting outputs.** Agent must check if its step file exists before writing. If it exists — STOP, log conflict, notify Source.
2. **Strict sequence.** Steps run in order: 1 → 2 → 3 → 4 → 5. No skipping.
3. **No agent writes to a future step.** OFFER-ARCHITECT writes only 01-offer.md. FUNNEL-ARCHITECT writes only 02-funnel.md. Etc.
4. **HUMANIZER mandatory.** Step 4 runs on every task. No exceptions.
5. **BRAND-GUARDIAN mandatory.** Step 5 runs on every task and assembles FINAL.md.
6. **Source approval required between each step.** Execution pauses after every step. Source decides before the next step starts.
7. **ORCHESTRATOR only assigns one step at a time.** No parallel execution.
8. **No agent marks a task DONE.** Only Source can set status = done.
9. **Output moves forward only.** A completed step is not re-executed unless Source explicitly resets it.

---

## SECTION 7 — LAUNCH REQUIREMENTS

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
- [ ] BRAND-GUARDIAN has reviewed all live pages
- [ ] HUMANIZER pass completed on all final copy
- [ ] Visual identity matches SYSTEM_RULES.md spec (black #050505, gold #d4af37, Inter font)

---

**Control remains with the Source. No step executes without a task. No output publishes without approval.**
