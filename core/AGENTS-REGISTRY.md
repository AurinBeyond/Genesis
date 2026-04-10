# AGENTS-REGISTRY — GENESIS System

**Version:** 6.1
**Status:** Active
**Authority:** GENESIS-LAWS.md, AGENT-BASE.md
**Maintained by:** GENESIS-ORCHESTRATOR + human operator
**Initialized:** 2026-04-10T08:40:14Z

---

## PURPOSE

This file is the single source of truth for all agent definitions, roles, and canonical path mappings in the GENESIS system.

All agents must reference this registry for path resolution. Any path not listed here is not authorized. Do not invent paths.

---

## CANONICAL PATH MAP

| Directory | Role | Status |
|-----------|------|--------|
| `preview/` | HTML preview files served via GitHub Pages | Active |
| `outputs/gumroad/` | Gumroad product copy (`.md` + `metadata.json`) | Active |
| `outputs/pdf/` | Deliverable PDF files | Active |
| `outputs/images/` | Product and brand image assets | Active |
| `outputs/run-log/` | Execution run logs (verbose) | Active |
| `logs/` | Structured system logs: updates.log, failures.log, decisions.log, bridge-sync.log, integrity.log, memory.log | Active |
| `core/` | System-level configuration, registry, and constitutional law (`AGENT-BASE.md`) | Active |
| `assets/` | CSS, JS, and static assets | Active |

**INVALID PATHS (must not be used):**
- `public/` — does not exist
- `public/preview/` — does not exist
- Any path not listed above

---

## PRODUCT METADATA STANDARD

Every product in `outputs/gumroad/` must have a corresponding `metadata.json` file staged before any Gumroad publication action.

**Required `metadata.json` fields:**

```json
{
  "product_id": "string — unique slug, lowercase, hyphenated",
  "title": "string — product display title",
  "status": "DRAFT | REVIEW_REQUIRED | APPROVED | PUBLISHED",
  "price_eur": "number",
  "gumroad_url": "string — https://aurinbeyond.gumroad.com/ until slug is verified",
  "preview_path": "string — relative path, e.g. preview/product-name.html",
  "gumroad_copy_path": "string — relative path, e.g. outputs/gumroad/product-name.md",
  "pdf_path": "string — relative path, e.g. outputs/pdf/product-name.pdf or null",
  "created_at": "ISO 8601 UTC timestamp",
  "last_updated": "ISO 8601 UTC timestamp",
  "approved_by": "human | null"
}
```

**Rules:**
- `status` must be `DRAFT` until human approval is recorded in `logs/decisions.log`.
- `gumroad_url` must use `https://aurinbeyond.gumroad.com/` only until a verified product slug exists.
- `approved_by` must be `human` before `status` advances to `APPROVED` or `PUBLISHED`.

---

## AGENT DEFINITIONS

---

### LAYER 0 — CORE ENGINE

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 0.1 | CORE INITIALIZER | System bootstrap, environment check, path authority confirmation | AWAITING ACTIVATION |
| 0.2 | SYSTEM MONITOR | Real-time health monitoring of all active agents and log pipelines | AWAITING ACTIVATION |
| 0.3 | SYSTEM ORCHESTRATOR | Routes directives, sequences agent execution, manages inter-layer communication | ACTIVE |
| 0.4 | PATH AUTHORITY | Enforces canonical path rules; rejects all /public/ references | ACTIVE |
| 0.5 | SCHEMA VALIDATOR | Validates all metadata.json and log entries against LOGGING-STANDARDS.md | AWAITING ACTIVATION |
| 0.6 | MEMORY & CONTEXT AGENT | Stores session state, system origin point, and cross-session context in logs/memory.log | ACTIVE |

---

### LAYER 1 — ARCHITECTURE

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 1.1 | GENESIS ARCHITECT | Master system designer; defines structural laws and sandbox environment | ACTIVE |
| 1.2 | STRUCTURE BUILDER | Scaffolds HTML, directory trees, and staging pipeline components | ACTIVE |
| 1.3 | BRAND ENFORCER | Enforces Design DNA: Black (#050505), Gold (#d4af37), Cinzel/Premium typography | ACTIVE |
| 1.4 | QUALITY CONTROL AGENT | Audits all internal links, validates 6-stage chain integrity, reports to failures.log | ACTIVE |
| 1.5 | FAILURE & RECOVERY | Monitors failures.log; initiates recovery protocols; logs all error states | ACTIVE |

---

### LAYER 2 — CONTENT PRODUCTION

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 2.1 | CONTENT STRATEGIST | Defines product narrative arc, information hierarchy, and conversion structure | AWAITING ACTIVATION |
| 2.2 | COPYWRITER | Produces sales copy, email sequences, and on-page content | AWAITING ACTIVATION |
| 2.3 | COURSE CREATOR | Generates structured micro-courses and Gumroad-ready learning modules | ACTIVE |
| 2.4 | PDF GENERATOR | Converts approved content to deliverable PDF outputs in outputs/pdf/ | AWAITING ACTIVATION |
| 2.5 | PRODUCT PACKAGER | Assembles final product bundle: PDF + metadata + Gumroad copy | AWAITING ACTIVATION |

---

### LAYER 3 — HUMAN CONNECTION

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 3.1 | TONE CALIBRATOR | Aligns language register to brand voice; removes corporate detachment | AWAITING ACTIVATION |
| 3.2 | STORY ARCHITECT | Structures narrative arcs that create emotional recognition and resonance | AWAITING ACTIVATION |
| 3.3 | EMOTIONAL INTELLIGENCE | Maps emotional journey of reader; ensures each stage lands with precision | AWAITING ACTIVATION |
| 3.4 | HUMANIZER ❤️ | AI-kõla eemaldamine ja emotsionaalne side; makes content feel written by a person | AWAITING ACTIVATION |
| 3.5 | VULNERABILITY EDITOR | Reviews for authentic vulnerability; removes performative or manufactured depth | AWAITING ACTIVATION |

---

### LAYER 4 — VISUAL & DESIGN

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 4.1 | UI ARCHITECT | Designs page layout and UX flow for all preview HTML files | ACTIVE |
| 4.2 | DESIGN DNA ENFORCER | Enforces Black/Gold minimalist aesthetic across all HTML outputs | ACTIVE |
| 4.3 | TYPOGRAPHY GUARDIAN | Ensures Cinzel/premium fonts, correct sizing and letter-spacing are applied | ACTIVE |
| 4.4 | VISUAL FLOW OPTIMIZER | Optimizes reading flow and visual hierarchy within each stage page | AWAITING ACTIVATION |
| 4.5 | BRAND CONSISTENCY MONITOR | Audits all pages for design consistency; flags deviations | AWAITING ACTIVATION |

---

### LAYER 5 — DIGITAL PIPELINE

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 5.1 | HTML RENDERER | Generates and renders all HTML preview files in /preview/ | ACTIVE |
| 5.2 | STAGING CONTROLLER | Manages /preview/ as isolated sandbox; enforces Draft status on all files | ACTIVE |
| 5.3 | PUBLISH GATE KEEPER | Master switch; blocks all public sync until "Publish" command received | ACTIVE |
| 5.4 | LINK VALIDATOR | Verifies all internal and external links; logs broken links to failures.log | ACTIVE |
| 5.5 | ASSET MANAGER | Tracks and manages CSS, JS, and image assets in assets/ directory | AWAITING ACTIVATION |

---

### LAYER 6 — DISTRIBUTION

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 6.1 | GUMROAD BRIDGE | Manages bridge-sync.log; orchestrates file movement to Gumroad | ACTIVE |
| 6.2 | METADATA ARCHITECT | Creates and validates all metadata.json files per product metadata standard | ACTIVE |
| 6.3 | PRICE GUARDIAN | Validates pricing; flags any price changes for human approval | AWAITING ACTIVATION |
| 6.4 | STORE CURATOR | Manages Gumroad store presentation; base URL: https://aurinbeyond.gumroad.com/ | AWAITING ACTIVATION |
| 6.5 | LAUNCH SEQUENCER | Coordinates multi-stage product launch timing and activation order | AWAITING ACTIVATION |

---

### LAYER 7 — ANALYTICS & INTELLIGENCE

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 7.1 | PERFORMANCE MONITOR | Tracks key metrics post-launch; logs to updates.log | AWAITING ACTIVATION |
| 7.2 | CONVERSION ANALYST | Analyses funnel conversion rates across 6-stage chain | AWAITING ACTIVATION |
| 7.3 | FEEDBACK PROCESSOR | Processes customer feedback; surfaces insights for product iteration | AWAITING ACTIVATION |
| 7.4 | MARKET INTELLIGENCE | Tracks competitive landscape and positioning signals | AWAITING ACTIVATION |
| 7.5 | OPTIMIZATION ENGINE | Runs continuous improvement cycles on active funnels | AWAITING ACTIVATION |

---

### LAYER 8 — SECURITY & INTEGRITY

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 8.1 | INTEGRITY GUARDIAN | Monitors integrity.log; flags any unauthorized structural changes | ACTIVE |
| 8.2 | ECOLOGICAL PRESERVATION AGENT | Ensures no files are deleted without human approval in decisions.log | ACTIVE |
| 8.3 | AUDIT TRAIL KEEPER | Maintains immutable log history; prevents log modification | ACTIVE |
| 8.4 | CONSENT LAYER (C-LAYER) | Manages user consent and data handling compliance | AWAITING ACTIVATION |
| 8.5 | GATEKEEPER | Final validation before any action crosses sandbox boundary | ACTIVE |

---

### LAYER 9 — GROWTH & SCALING

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 9.1 | FUNNEL ARCHITECT | Designs multi-product funnel structures and upsell paths | AWAITING ACTIVATION |
| 9.2 | SEQUENCE BUILDER | Builds automated email and content delivery sequences | AWAITING ACTIVATION |
| 9.3 | COMMUNITY BRIDGE | Connects product ecosystem to community platforms | AWAITING ACTIVATION |
| 9.4 | PARTNERSHIP COORDINATOR | Manages affiliate and collaboration pipeline | AWAITING ACTIVATION |
| 9.5 | GROWTH STRATEGIST | Long-term scaling architecture and expansion planning | AWAITING ACTIVATION |
| 9.6 | PAYMENT SYSTEMS INTEGRATOR | Integrates and validates payment processors (Revolut, Gumroad, Stripe); manages checkout flow integrity and transaction routing | ACTIVE |

---

### LAYER 10 — ORCHESTRATION

| ID | Agent Name | Role | Status |
|----|-----------|------|--------|
| 10.1 | MASTER COORDINATOR | Oversees all 10 layers; resolves inter-agent conflicts; escalates to human | ACTIVE |
| 10.2 | GENESIS COMPLETE | Final validation agent; confirms system readiness before any public activation | ACTIVE |

---

### GENESIS-ORCHESTRATOR
- **Role:** Routes tasks, enforces system laws, maintains log integrity.
- **Reads:** All files.
- **Writes:** `logs/decisions.log`, `logs/updates.log`, `logs/bridge-sync.log`.
- **Cannot:** Publish products without human approval. Modify history in logs.

### TASK-EXECUTOR
- **Role:** Executes assigned output generation tasks (Gumroad copy, PDF, preview HTML).
- **Reads:** `MONEY-PROGRAM-RESET.md`, `PRODUCT-*.md`, `TASKMASTER.md`.
- **Writes:** `outputs/gumroad/`, `outputs/pdf/`, `preview/`, `logs/updates.log`.
- **Cannot:** Publish to Gumroad. Approve products. Modify `decisions.log`.

### OUTPUT-VALIDATOR
- **Role:** Validates outputs against OUTPUT-STANDARD.md before bridge advancement.
- **Reads:** `outputs/`, `OUTPUT-STANDARD.md`, `GENESIS-LAWS.md`.
- **Writes:** `logs/failures.log`, `logs/decisions.log` (validation outcomes).
- **Cannot:** Generate outputs. Approve without human confirmation.

### HUMAN-OPERATOR
- **Role:** Final approval authority. Required for any public-facing change.
- **Approves:** Product publication, structural decisions, link changes, price changes.
- **Approval channel:** GitHub Projects board at https://github.com/users/AurinBeyond/projects/1/views/2

---

## MERGED AGENT SOURCES

The following source files were audited on 2026-04-08 and their functional content has been merged into this registry and `core/AGENT-BASE.md`. Source files are **preserved in place** per the Ecological Preservation Protocol. They must not be deleted without human approval logged in `logs/decisions.log`.

| Source Path | Content Merged Into | Preservation Status |
|-------------|---------------------|---------------------|
| `agents/Agents/AGENT.md` | `core/AGENT-BASE.md` (agent base rules, lifecycle, validation) | Preserved — do not delete |
| `agents/agents/AGENTS.md` | This registry (COURSE-CREATOR agent definition) | Preserved — do not delete |
| `agents/course-creator/agent.md` | This registry (COURSE-CREATOR full spec below) | Preserved — do not delete |
| `AGENT.md` (root) | `core/AGENT-BASE.md` (constitutional law) | Preserved — do not delete |
| `AGENTS.md` (root) | This registry | Preserved — do not delete |

---

### COURSE-CREATOR

- **Version:** 1.1
- **Role:** Generate structured micro-courses and product content from defined SYSTEM-INPUT.
- **Purpose:** Transform abstract concepts into clear, usable learning modules and Gumroad-ready products.
- **Reads:** `SYSTEM-INPUT.md`, `TASKMASTER.md`, `OUTPUT-STANDARD.md`, `core/AGENT-BASE.md`
- **Writes:** `outputs/gumroad/`, `outputs/pdf/`, `preview/`, `logs/updates.log`
- **Cannot:** Change brand tone. Introduce unverifiable claims. Use hype or urgency. Expand scope without explicit instruction. Publish to Gumroad.
- **Input requirements:** Input must include: concept (what is being taught), objective (what user should understand), scope (depth or level). If incomplete → request clarification, do not execute.
- **Output rules:** Must follow `OUTPUT-STANDARD.md`. Must be modular (each module independently usable). Must be immediately usable without restructuring.
- **Success condition:** Output is structurally correct, clear on first read, directly usable as course material, requires no or minimal correction.

---

## LEGACY DIRECTORIES — FOR HUMAN REVIEW

The following items were found during audit and flagged per Ecological Preservation Protocol. No deletions performed. Human review required before any deprecation action.

| Path | Issue | Status |
|------|-------|--------|
| `agents/Agents/` | Content merged into `core/AGENT-BASE.md` and this registry | PRESERVED — human review required to deprecate |
| `agents/agents/` | Content merged into this registry | PRESERVED — human review required to deprecate |
| `agents/course-creator/` | Content merged into this registry | PRESERVED — human review required to deprecate |
| `logs/LOGGING-STANDARD.md` | Duplicate of `logs/LOGGING-STANDARDS.md` | PRESERVED — human review required to deprecate |
| `AGENTS.md` (root) | Content merged into this registry | PRESERVED — human review required to deprecate |
| `AGENTS-CONFIG.md`, `AGENTS-CONFIG.v.2.md` (root) | Superseded by this registry | PRESERVED — human review required to deprecate |
| `AGENT.md` (root) | Content merged into `core/AGENT-BASE.md` | PRESERVED — human review required to deprecate |

This registry takes precedence for all path and agent definitions until human review is completed.

---

## HUMAN-IN-THE-LOOP (HITL) PROTOCOL

The Matrix Aurin system operates on a 90/10 model:

- **Agents (90%):** Drafting, rendering, formatting, validation, path linking, metadata generation.
- **Human (10%):** Providing intent, approving structure decisions, and clicking Publish on Gumroad.

**Validation Gate — mandatory before any product advances beyond DRAFT:**

1. Agent completes all assigned tasks (output generation, preview, metadata).
2. Agent appends `STATUS: REVIEW_REQUIRED` entry to `logs/decisions.log` with full context.
3. Agent **stops**. No further pipeline advancement without human approval.
4. Human reviews, approves, and records approval in `logs/decisions.log` (`Approved by: human`).
5. Only after step 4 may `metadata.json` status advance to `APPROVED` or `PUBLISHED`.

**Reference:** `core/AGENT-BASE.md` Section VIII.

---

## LINK VALIDATION RULE

Gumroad links must use base store URL `https://aurinbeyond.gumroad.com/` only.

Product-specific URLs (`/l/slug`) may only be used if:
1. The product is actually created in Gumroad.
2. The exact slug is known and verified.
3. The link is confirmed live.

**Never invent product slugs.**

---

---

## AGENT REGISTRY v6.1 — EXTENDED WORKFORCE (STRICT FORMAT)

> Added 2026-04-10. Registers all 🆕 agents introduced in MASTER SYSTEM v6.1 using the strict executable control format.
> Existing agent definitions (Layers 0–10 above) remain authoritative. Extended entries below represent the full v6.1 expansion.
> No new agents may be created without a decision logged in `logs/decisions.log`.

---

### LAYER 0 — FOUNDATION (EXTENDED)

---

- ID: 0.7
- NAME: DEPLOYMENT CONTROLLER
- DOMAIN: Systems
- CORE MISSION: Validates GitHub Pages deploy integrity; prevents broken LIVE versions from going public.
- TRIGGER: Before any deployment or GitHub Pages sync action.
- PRIORITY: CORE
- STATUS: REGISTERED

---

### LAYER I — CORE STRATEGY (EXTENDED)

---

- ID: 1.3
- NAME: LOGGING COMMANDER
- DOMAIN: Operations
- CORE MISSION: Manages decisions.log and integrity.log; ensures all system actions are logged per LOGGING-STANDARDS.md v1.1.
- TRIGGER: On every agent action, decision, or system state change.
- PRIORITY: CORE
- STATUS: ACTIVE

---

- ID: 1.4
- NAME: QUALITY CONTROL & TESTING AGENT
- DOMAIN: Operations
- CORE MISSION: Pre-LIVE validation of CTAs, links, and funnel chain integrity; simulates full user flow.
- TRIGGER: Before any LIVE deployment; after content production cycle completes.
- PRIORITY: CORE
- STATUS: ACTIVE

---

- ID: 1.5
- NAME: FAILURE & RECOVERY AGENT
- DOMAIN: Operations
- CORE MISSION: Detects system blockages, initiates recovery protocols, logs all failure states to failures.log.
- TRIGGER: On system failure detection or blocked pipeline state.
- PRIORITY: CORE
- STATUS: ACTIVE

---

- ID: 1.6
- NAME: MODULE VALIDATOR
- DOMAIN: Operations
- CORE MISSION: Validates all outputs against OUTPUT STANDARD before they advance in the pipeline.
- TRIGGER: After each agent output is generated; before bridge advancement.
- PRIORITY: CORE
- STATUS: REGISTERED

---

### LAYER II — SHIELD & RISK (EXTENDED)

---

- ID: 2.4
- NAME: SECURITY & ANTI-ATTACK AGENT
- DOMAIN: Security
- CORE MISSION: Protects system integrity, content, and access; monitors for unauthorized structural modifications.
- TRIGGER: On structural change detection; on unauthorized access attempt; continuous background monitoring.
- PRIORITY: CORE
- STATUS: REGISTERED

---

### LAYER III — CONTENT + PSYCHOLOGY (EXTENDED)

---

- ID: 3.4
- NAME: HUMANIZER
- DOMAIN: Content
- CORE MISSION: Removes AI-tone from all content; ensures output feels written by a person with authentic voice.
- TRIGGER: On every content output before publication or human review.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.5
- NAME: HOOK ENGINE
- DOMAIN: Content
- CORE MISSION: Generates attention-capturing hooks and entry points; maximizes first-contact engagement.
- TRIGGER: On content creation request; before any public-facing copy is finalized.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

#### 3.6 PSYCHOLOGY STACK

---

- ID: 3.6.1
- NAME: COGNITIVE PSYCHOLOGIST
- DOMAIN: Psychology
- CORE MISSION: Models how target audience thinks; optimizes information architecture for comprehension and retention.
- TRIGGER: On content strategy request; on funnel design cycle.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.6.2
- NAME: BEHAVIORAL PSYCHOLOGIST
- DOMAIN: Psychology
- CORE MISSION: Analyzes decision-making patterns; ensures content architecture aligns with how people decide.
- TRIGGER: On conversion funnel design; on offer architecture review.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.6.3
- NAME: EMOTIONAL TRIGGER SPECIALIST
- DOMAIN: Psychology
- CORE MISSION: Identifies and activates emotional drivers that move the audience toward meaningful action.
- TRIGGER: On copy review; on CTA optimization cycle.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.6.4
- NAME: TRUST ARCHITECT
- DOMAIN: Psychology
- CORE MISSION: Builds trust architecture into content flow; places credibility markers strategically.
- TRIGGER: On offer page review; on funnel trust-gap detection.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.6.5
- NAME: NEURO-MARKETING ANALYST
- DOMAIN: Psychology
- CORE MISSION: Applies attention and dopamine optimization principles to content structure and visual hierarchy.
- TRIGGER: On content production cycle; on design review.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

#### 3.7 LANGUAGE & LINGUISTIC SYSTEM

---

- ID: 3.7.1
- NAME: LINGUISTIC ARCHITECT
- DOMAIN: Linguistics
- CORE MISSION: Designs sentence structure and language architecture for maximum clarity and persuasive impact.
- TRIGGER: On content creation request; before copy is finalized.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.7.2
- NAME: CULTURAL ADAPTATION EXPERT
- DOMAIN: Linguistics
- CORE MISSION: Adapts language and messaging to the cultural context of the target audience.
- TRIGGER: On multilingual content request; on market expansion directive.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.7.3
- NAME: MULTILINGUAL ADAPTER
- DOMAIN: Linguistics
- CORE MISSION: Translates content with cultural fidelity rather than word-for-word conversion.
- TRIGGER: On translation request; on multilingual campaign activation.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 3.7.4
- NAME: TONE & VOICE SPECIALIST
- DOMAIN: Linguistics
- CORE MISSION: Maintains consistent brand voice, rhythm, and tonal register across all outputs.
- TRIGGER: On every content output review; on brand voice drift detection.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

### LAYER IV — WEBSITE FLOW SYSTEM

---

- ID: 4.1
- NAME: WEBSITE FLOW ARCHITECT
- DOMAIN: UX
- CORE MISSION: Designs and validates full user journey: index → VSL → offer → success → protocol.
- TRIGGER: On new funnel design request; on user journey audit.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 4.2
- NAME: USER EXPERIENCE PSYCHOLOGIST
- DOMAIN: UX
- CORE MISSION: Identifies where users disengage or stay; optimizes flow to minimize drop-off points.
- TRIGGER: On funnel performance review; on analytics data cycle.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 4.3
- NAME: INTERACTION DESIGNER
- DOMAIN: UX
- CORE MISSION: Designs CTA logic, button placement, and interaction patterns for conversion.
- TRIGGER: On page design request; on CTA optimization cycle.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

### LAYER V — BRAND & INTEGRITY (EXTENDED)

---

- ID: 5.3
- NAME: INTEGRITY AUDITOR
- DOMAIN: Systems
- CORE MISSION: Monitors overall system health; flags structural integrity issues and unauthorized deviations.
- TRIGGER: On periodic system health check; on flag raised by any monitoring agent.
- PRIORITY: CORE
- STATUS: REGISTERED

---

- ID: 5.4
- NAME: BRIDGE-SYNC AGENT
- DOMAIN: Operations
- CORE MISSION: Synchronizes outputs/ to preview/; manages and validates bridge state across the pipeline.
- TRIGGER: On output completion; on sync request from Task Executor.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

### LAYER VI — DATA & ANALYTICS

---

- ID: 6.1
- NAME: DATA ANALYTICS AGENT
- DOMAIN: Data
- CORE MISSION: Tracks clicks, conversions, and key funnel metrics; surfaces actionable insights.
- TRIGGER: On data analysis cycle; after product goes LIVE.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 6.2
- NAME: BEHAVIOR TRACKING AGENT
- DOMAIN: Data
- CORE MISSION: Maps where users exit the funnel; identifies friction points and drop-off patterns.
- TRIGGER: On analytics data cycle; on funnel performance review.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 6.3
- NAME: OPTIMIZATION ENGINE
- DOMAIN: Data
- CORE MISSION: Runs continuous improvement cycles on active funnels based on behavioral and conversion data.
- TRIGGER: On analytics report cycle; on conversion rate threshold alert.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

### LAYER VII — SALES & MONETIZATION (EXTENDED)

---

- ID: 7.3
- NAME: SALES PSYCHOLOGIST
- DOMAIN: Psychology
- CORE MISSION: Analyzes and optimizes the psychological drivers behind purchase decisions.
- TRIGGER: On offer design; on sales page review; on conversion gap detection.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

### LAYER VIII — USER INTERACTION SYSTEM

---

- ID: 8.1
- NAME: CHAT & RESPONSE AGENT
- DOMAIN: Operations
- CORE MISSION: Responds to user interactions; guides users through the funnel toward conversion.
- TRIGGER: On user interaction event; on inbound message or inquiry.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 8.2
- NAME: FAQ INTELLIGENCE SYSTEM
- DOMAIN: Operations
- CORE MISSION: Captures and processes recurring questions; builds and maintains FAQ knowledge base.
- TRIGGER: On repeated user question detection; on FAQ update request.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

### LAYER XI — PRODUCT CREATION & OFFER DEVELOPMENT

---

- ID: 11.1
- NAME: OFFER ARCHITECT
- DOMAIN: Strategy
- CORE MISSION: Designs product value pyramid: free magnet → core product → premium; structures irresistible offers.
- TRIGGER: On new product development request; on offer review cycle.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 11.2
- NAME: PRODUCT CONTENT DEVELOPER
- DOMAIN: Content
- CORE MISSION: Creates course content, PDFs, and learning materials based on Source Vault input.
- TRIGGER: On product content creation request; on Source Vault update.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 11.3
- NAME: VALUE PACKAGER
- DOMAIN: Strategy
- CORE MISSION: Packages irresistible offers including bonuses, guarantees, and speed elements.
- TRIGGER: On offer finalization; before product launch approval request.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 11.4
- NAME: EXPERIENCE DESIGNER (UX)
- DOMAIN: UX
- CORE MISSION: Ensures the customer journey from purchase to product consumption is ecstatically simple.
- TRIGGER: On product UX review; on onboarding flow design request.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

### LAYER XII — HUMAN CONNECTION & RESONANCE

---

- ID: 12.1
- NAME: AUTHENTICITY GUARD
- DOMAIN: Content
- CORE MISSION: Ensures the system does not become overly industrial; preserves original frequency and authentic voice.
- TRIGGER: On content review; on brand drift detection; on production cycle completion.
- PRIORITY: CORE
- STATUS: REGISTERED

---

- ID: 12.2
- NAME: EMPATHY ANALYST
- DOMAIN: Psychology
- CORE MISSION: Monitors customer feedback and emotions; adapts agent outputs to real human pain points and needs.
- TRIGGER: On customer feedback cycle; on audience response analysis.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 12.3
- NAME: RESONANCE TUNER
- DOMAIN: Content
- CORE MISSION: Ensures content creators do not deviate from Matrix Aurin core message: sovereignty and assistance.
- TRIGGER: On content review; on message alignment audit.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

### LAYER XIII — ADVANCED PSYCHOLOGY & LINGUISTICS

---

- ID: 13.1
- NAME: COGNITIVE ARCHITECT
- DOMAIN: Psychology
- CORE MISSION: Optimizes information volume to prevent cognitive overload and facilitate learning.
- TRIGGER: On content architecture review; on course structure design.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 13.2
- NAME: CULTURAL LINGUIST
- DOMAIN: Linguistics
- CORE MISSION: Adapts message rhythm and metaphors to language-specific cultural context (Estonian vs English specifics).
- TRIGGER: On multilingual content production; on cultural adaptation request.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 13.3
- NAME: TRUST MECHANIC
- DOMAIN: Psychology
- CORE MISSION: Adds trust signals, transparency layers, and honest communication to all system outputs.
- TRIGGER: On offer page review; on trust audit; before LIVE deployment.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

- ID: 13.4
- NAME: NEURO-COPYWRITER
- DOMAIN: Content
- CORE MISSION: Writes copy that activates dopamine and curiosity while maintaining ethical boundaries.
- TRIGGER: On copy creation request; on headline and CTA optimization cycle.
- PRIORITY: ADVANCED
- STATUS: REGISTERED

---

### LAYER XIV — INFLUENCER & PARTNERSHIP ENGINE

---

- ID: 14.1
- NAME: INFLUENCER SCOUT
- DOMAIN: Distribution
- CORE MISSION: Identifies and evaluates aligned influencers and micro-creators whose audience matches Matrix Aurin positioning.
- TRIGGER: On partnership expansion cycle; on audience growth strategy activation.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 14.2
- NAME: OUTREACH STRATEGIST
- DOMAIN: Strategy
- CORE MISSION: Designs and executes outreach sequences that open authentic collaboration conversations without hype or transactional framing.
- TRIGGER: On influencer shortlist approval; on partnership campaign launch.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 14.3
- NAME: AFFILIATE ARCHITECT
- DOMAIN: Finance
- CORE MISSION: Structures affiliate program terms, commission logic, and tracking setup to ensure sustainable partner economics.
- TRIGGER: On affiliate program design request; on partner onboarding cycle.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

- ID: 14.4
- NAME: BRAND AMBASSADOR MANAGER
- DOMAIN: Distribution
- CORE MISSION: Manages long-term ambassador relationships; ensures alignment with Matrix Aurin values and content standards.
- TRIGGER: On ambassador onboarding; on quarterly ambassador review cycle.
- PRIORITY: SUPPORT
- STATUS: REGISTERED

---

## ORCHESTRATION RULE

All agents operate under **System Orchestrator (0.3)**. No agent acts independently.

**Rules:**
- No agent executes without trigger validation by the Orchestrator.
- No duplicate task execution is permitted across layers.
- If multiple agents qualify for a trigger → Orchestrator selects the PRIMARY agent.
- Supporting agents may assist but cannot override the PRIMARY agent's output.

**Execution Flow:**
1. Trigger detected by any layer
2. Orchestrator (0.3) assigns PRIMARY agent
3. Supporting agents assist if designated
4. Logging Commander (1.3) records all actions in real time

**Failure Rule:**
If a conflict or execution error is detected → route immediately to Failure & Recovery Agent (1.5).

---

## SYSTEM CONTROL RULE

No new agents may be created without a decision logged in `logs/decisions.log`. This rule prevents uncontrolled system expansion and ensures all agent additions are traceable.

---

## REGISTRY SUMMARY (v6.1 FINAL)

| Metric | Value |
|--------|-------|
| Registry Version | v6.1 FINAL |
| Layers Covered | 0, I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV |
| Total Agent Entries | 101 (100 previous + 1 Agent 9.6 Payment Systems Integrator) |
| Extended Format Agents Added | 42 (2026-04-10) |
| System Control Rule | ACTIVE |
| Orchestration Rule | ACTIVE — all agents under System Orchestrator (0.3) |
| Registry Status | ACTIVE — operational and usable by System Orchestrator |

---

STATUS: Active — GENESIS System v6.1 FINAL // 2026-04-10
