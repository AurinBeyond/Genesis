# AGENTS-REGISTRY — GENESIS System

**Version:** 1.1
**Status:** Active
**Authority:** GENESIS-LAWS.md, AGENT-BASE.md
**Maintained by:** GENESIS-ORCHESTRATOR + human operator

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
| `logs/` | Structured system logs: updates.log, failures.log, decisions.log, bridge-sync.log, integrity.log | Active |
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

STATUS: Active — GENESIS System // 2026-04-08
