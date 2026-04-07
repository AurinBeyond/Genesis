# 🧭 GENESIS SYSTEM INDEX v1.0

## PURPOSE
This file defines the valid structure of the repository.
Agents MUST follow this structure.

---

## 📁 ALLOWED DIRECTORIES

core/
agents/
laws/
logs/
archive/
.github/
scripts/

---

## 📁 CORE

core/
├── GENESIS-LAWS.md
├── INPUT.md
├── MODE.md
├── OUTPUT-STANDARD.md
├── STATE.md
├── SYSTEM-INPUT.md
└── TASK.md

---

## 📁 AGENTS

agents/
├── AGENT-BASE.md
├── AGENTS-REGISTRY.md
├── templates/
│   └── AGENT-TEMPLATE.md
├── course-creator/
│   └── agent.md

---

## 📁 ARCHIVE

archive/
└── core/
    └── AGENTS-CONFIG.v.2.md

---

## 📁 RULES

1. Do NOT create new root-level folders
2. Do NOT duplicate files
3. If file exists → UPDATE, do NOT recreate
4. If structure mismatch → STOP execution
5. All changes must follow this index

---

## 🔒 VALIDATION

Before any write:
- Check if path exists
- Check if file exists
- Check if modification is allowed

If ANY check fails:
→ STOP

---

## STATUS

System structure is LOCKED
