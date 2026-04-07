# SYSTEM-ARCHITECTURE.md
# AurinBeyond / Genesis
# Version: 1.0
# Date: 2026-04-07
# Status: BLUEPRINT — Structure definition only. No files modified.

---

## SECTION 1 — CORE PRINCIPLE

> **Genesis is NOT a platform like Gumroad.**
> **Genesis is a control system that connects to platforms.**

Genesis does not sell, host, or deliver products directly. It orchestrates the agents, logic, and content pipelines that connect to platforms (Gumroad, Stripe, etc.) which handle delivery and payment.

This distinction is the foundation of every structural decision in this repository:

- Platforms = external. They are integrations, not part of the system core.
- Genesis = internal. It controls, coordinates, and outputs — it does not replace the platforms.
- The system exists to produce and route. It does not exist to be a product itself.

---

## SECTION 2 — TARGET REPOSITORY STRUCTURE

The following is the clean, final target structure. Every file and folder has exactly one responsibility. No exceptions.

```
/
├── public/                     → Frontend only (HTML landing pages, VSL, offer, legal)
│   ├── index.html
│   ├── offer.html
│   ├── gateway.html
│   ├── vsl.html
│   ├── success.html
│   ├── terms.html
│   └── (all other HTML pages)
│
├── assets/                     → Static assets only (CSS, JS, images)
│   ├── css/
│   └── js/
│
├── core/                       → System logic only (laws, state, input/output definitions)
│   ├── GENESIS-LAWS.md
│   ├── STATE.md
│   ├── INPUT.md
│   ├── OUTPUT-STANDARD.md
│   ├── MODE.md
│   └── TASK.md
│
├── agents/                     → ALL agents (single authoritative source, no duplicates)
│   ├── AGENT-REGISTRY.md       → Master registry of all agents
│   ├── AGENT-BASE.md           → Base behavior definition for all agents
│   ├── templates/
│   │   └── AGENT-TEMPLATE.md
│   └── (one subfolder per agent, named by agent role)
│       └── course-creator/
│           └── agent.md
│
├── orchestration/              → Execution logic only
│   └── ORCHESTRATOR-FLOW.md
│
├── integrations/               → External system connectors (Gumroad, Stripe, etc.)
│   └── (one file or folder per integration)
│
├── logs/                       → System state and output logs only
│   ├── updates.log
│   ├── state-tracker.md
│   └── outputs/
│
├── archive/                    → Deprecated files only (read-only, not executed)
│
├── scripts/                    → Automation scripts only
│   └── normalize-structure.sh
│
├── .github/
│   └── workflows/              → CI / agent execution pipelines
│
├── README.md                   → Public-facing project description
├── TASKMASTER.md               → Active task queue
├── SYSTEM-INDEX.md             → Repository structure index
├── SYSTEM-ARCHITECTURE.md      → This file (structural blueprint)
└── SYSTEM_RULES.md             → Visual and brand rules
```

---

## SECTION 3 — STRUCTURAL RULES

These rules are strict and not negotiable. Any file that violates them is structurally invalid.

1. **No agents outside `/agents/`.**
   - There is no `/GENESIS/agents/`, no root-level agent files, no agent definitions inside `/core/`.
   - Every agent definition lives in `/agents/` and is registered in `AGENT-REGISTRY.md`.

2. **No frontend logic in `/core/`.**
   - `/core/` contains only system laws, state definitions, and input/output standards.
   - HTML, CSS, JavaScript, and page copy belong exclusively in `/public/` and `/assets/`.

3. **No orchestration inside agents.**
   - Agents do not call other agents.
   - Agents do not determine their own activation sequence.
   - All orchestration is defined in `/orchestration/ORCHESTRATOR-FLOW.md`.

4. **No duplication of files across folders.**
   - A file exists in exactly one location.
   - Superseded versions are moved to `/archive/`, not left in place alongside the new version.

5. **Each folder has ONE responsibility only.**
   - `/core/` = system logic. Not content, not agents, not UI.
   - `/agents/` = execution units. Not laws, not UI, not orchestration.
   - `/public/` = frontend. Not logic, not agents, not state.
   - `/integrations/` = external connections. Not internal logic.
   - `/logs/` = output and state history. Not definitions.
   - `/archive/` = deprecated material. Not active in any pipeline.

6. **Root-level files are system-wide references only.**
   - The repository root contains only files that apply to the whole system: README, TASKMASTER, SYSTEM-INDEX, SYSTEM-ARCHITECTURE, SYSTEM_RULES, GENESIS-LAWS equivalents.
   - Operational files (agent configs, orchestration, templates) belong in their respective folders.

---

## SECTION 4 — AGENT SYSTEM POSITION

The agent system follows a strict hierarchy. No agent operates outside this hierarchy.

```
TASKMASTER (input)
    ↓
ORCHESTRATOR (determines sequence)
    ↓
AGENT (executes assigned task)
    ↓
OUTPUT (written to /logs/outputs/)
```

**Definitions:**

- **Agents** = execution units. Each agent has a single, defined responsibility. Agents receive input and produce output. They do not self-activate, do not modify other agents' files, and do not define system rules.

- **AGENT-REGISTRY.md** = single source of truth for all agents. An agent that is not in the registry does not exist in the system. An agent that is in the registry but has no definition file is considered inactive. No agent may be invoked if it is absent from the registry.

- **Orchestrator** = controls execution sequence. It reads the task from TASKMASTER, selects the appropriate agent(s) in the correct order, and hands off input. The orchestrator does not produce content itself.

- **Agents never self-activate.** An agent executes only when called by the orchestrator. An agent that appears in code, a workflow, or a task file but is not registered in AGENT-REGISTRY.md is an unauthorized agent and must be flagged.

---

## SECTION 5 — GUMROAD LESSON (ABSTRACTED)

**Do NOT replicate Gumroad.**
**Do NOT import its structure directly.**
**Do NOT use it as a naming reference.**

Gumroad is a commerce platform. Genesis is a control system. They are not comparable at the implementation level. Copying Gumroad's structure would be a category error.

**What Gumroad demonstrates (architecture principles only):**

| Principle | What Gumroad shows | How Genesis applies it |
|---|---|---|
| Separation of concerns | Frontend, backend, payments, and data are in distinct layers with defined interfaces | `public/`, `core/`, `agents/`, `integrations/` are completely isolated from each other |
| Deterministic execution | Every action follows a defined pipeline; nothing is ambiguous | ORCHESTRATOR-FLOW defines exact agent call sequence; no agent self-activates |
| Centralized control | A single system controls routing and state | AGENT-REGISTRY is the single source of truth; TASKMASTER is the single input point |

The lesson from Gumroad is not structural imitation. It is the principle that **clear layers make systems scalable and debuggable**. Genesis applies this principle to its own domain.

---

## SECTION 6 — CURRENT PROBLEMS (DIAGNOSIS)

The following structural problems exist in the current repository state. They are explicit violations of the architecture defined in this document.

### Problem 1: Duplicated agent folders
- `/agents/` exists.
- Historical references to `/GENESIS/agents/` exist in archive files.
- Agent-like content (COURSE-CREATOR) exists in `/archive/agents-agents-AGENTS.md`.
- **Impact:** No single source of truth for agents. Registry creation is blocked.

### Problem 2: Missing central registry
- `agents/AGENTS-REGISTRY.md` exists but is a generic placeholder with 4 technical agents (GENESIS-ORCHESTRATOR, TASK-EXECUTOR, OUTPUT-VALIDATOR, SYSTEM-AUDITOR).
- No MASTER SYSTEM STRUCTURE defining official agents by layer exists.
- **Impact:** It is not possible to verify which agents are authorized. The system cannot validate agent calls.

### Problem 3: Unclear activation logic
- `ORCHESTRATOR-FLOW.md` exists in `/agents/` instead of `/orchestration/`.
- The file was reconstructed from task prompts rather than from a committed source document.
- TASKMASTER.md references `@LanguageAgent` — a name not defined in any registry.
- **Impact:** Agents cannot be reliably invoked because the orchestration path is ambiguous.

### Problem 4: Mixed frontend and system files
- HTML files exist in both `/public/` and scattered root-level locations (e.g., `11.7 Gatekeeper (Consent C-Layer`, `The Gatekeeper`).
- Root-level files include non-system content (Estonian-language OS narrative files: `ARKANA-OS`, `PROTOCOL CORE ENGINE 01`).
- **Impact:** Repository has no clear boundary between the system and its outputs.

### Problem 5: Unstructured root level
- Files with spaces in names exist at root (`Clean repository root structure`, `Extended Description`, `Agents`, `site`).
- These are fragments from previous sessions that were committed as-is.
- **Impact:** The root layer is not clean. SYSTEM-INDEX.md does not match actual root contents.

---

## SECTION 7 — MIGRATION PLAN

These are the exact steps required to move the repository from its current state to the target architecture. Steps are ordered by dependency. No step should be executed before the preceding step is complete.

**Step 1: Establish `/agents/` as the single source**
- Confirm `agents/AGENT-BASE.md` and `agents/templates/AGENT-TEMPLATE.md` are in place. ✓
- Confirm `agents/course-creator/agent.md` is the only active agent definition file. ✓

**Step 2: Create the authoritative MASTER SYSTEM STRUCTURE**
- Commit a file (suggested: `core/MASTER-SYSTEM-STRUCTURE-v5.md`) that defines the complete, official agent list with layer assignments (Layer 0 → IX) and an explicit agent count.
- This is a prerequisite for Step 3.

**Step 3: Create `agents/AGENT-REGISTRY.md`**
- Only after Step 2 is complete.
- Source every agent name, ID, and layer from the MASTER SYSTEM STRUCTURE file created in Step 2.
- Remove `agents/AGENT-REGISTRY-BLOCKER-REPORT.md` once the registry is created and validated.

**Step 4: Move orchestration**
- Create `/orchestration/` directory.
- Move `agents/ORCHESTRATOR-FLOW.md` → `orchestration/ORCHESTRATOR-FLOW.md`.
- Update all references to the old path.

**Step 5: Clean the root level**
- Move `ARKANA-OS`, `PROTOCOL CORE ENGINE 01`, `SYSTEM RULES v1.2`, `11.7 Gatekeeper (Consent C-Layer`, `The Gatekeeper`, `Agents`, `Clean repository root structure`, `Extended Description`, `site` to `/archive/` or delete if confirmed obsolete.
- Root should contain only: `README.md`, `TASKMASTER.md`, `SYSTEM-INDEX.md`, `SYSTEM-ARCHITECTURE.md`, `SYSTEM_RULES.md`, `AGENTS.md`, `AGENTS-CONFIG.md`, `OUTPUT.md`, `arkana-core-taskmaster.md`, `arkana-pipeline.yml`, `updates.log`.

**Step 6: Create `/integrations/`**
- Create the directory.
- Document any external platform connections (Gumroad, Stripe, Google Analytics) as integration definition files.

**Step 7: Separate and clean `/public/`**
- Audit all HTML files. Confirm they are all in `/public/`.
- Move any HTML files found outside `/public/` into it.
- Remove duplicate or fragment HTML files.

**Step 8: Archive obsolete files**
- All deprecated agent definitions, old AGENTS.md variants, and root fragments move to `/archive/`.
- Archive files are never executed. They are reference-only.

**Step 9: Update `SYSTEM-INDEX.md`**
- After all moves are complete, update `SYSTEM-INDEX.md` to reflect the actual, final structure.
- `SYSTEM-INDEX.md` is the map of the system. It must be accurate.

---

## SECTION 8 — CONTROL GUARANTEE

> **If a file is not in its correct layer, it is invalid.**

This is not a preference. It is the enforcement rule of this architecture.

- An agent not in `/agents/` is not an authorized agent.
- An agent not in `AGENT-REGISTRY.md` does not exist in the system.
- Orchestration logic not in `/orchestration/` is not the official execution sequence.
- Frontend files not in `/public/` are structurally misplaced.
- System logic not in `/core/` is not authoritative.

Any automated pipeline, agent execution, or human contributor that places a file outside its defined layer must be corrected before the file can be considered part of the active system.

This guarantee is what makes the system scalable, auditable, and controllable.

---

*This file is a structure definition only. No files were modified during its creation.*
*All implementation steps are defined in Section 7.*
*This file is the blueprint for all future structural changes to this repository.*
