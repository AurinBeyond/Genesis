# AGENTS-REGISTRY — GENESIS System

**Version:** 1.0
**Status:** Active
**Authority:** GENESIS-LAWS.md
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
| `logs/` | Structured system logs | Active |
| `core/` | System-level configuration and registry | Active |
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

## CONFLICTING DIRECTORIES — RESOLUTION

The following directories were found during the 2026-04-08 audit and require resolution:

| Path | Issue | Action Required |
|------|-------|-----------------|
| `agents/` | Contains subdirectories `Agents/`, `agents/`, `course-creator/` — no single standard | Human decision required to consolidate or deprecate |
| `logs/LOGGING-STANDARD.md` | Duplicate of `logs/LOGGING-STANDARDS.md` | Human decision required to deprecate |
| `AGENTS.md`, `AGENTS-CONFIG.md`, `AGENTS-CONFIG.v.2.md`, `AGENT.md` | Multiple agent config files at root | Human decision required; this file (AGENTS-REGISTRY.md) is now canonical |

Until resolved, this registry takes precedence for all path and agent definitions.

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
