# logs/outputs/

This directory stores agent outputs awaiting Source review.

## Structure
Each task gets its own folder:

```
logs/outputs/TASK-XXX/
  01-offer.md       ← OFFER-ARCHITECT output
  02-funnel.md      ← FUNNEL-ARCHITECT output
  03-content.md     ← CONTENT-PRODUCER output
  04-humanized.md   ← HUMANIZER output
  FINAL.md          ← assembled after all steps approved
```

## Rules
- Each agent writes ONLY its own step file.
- Agent must NOT overwrite an existing file.
- Each step requires Source approval before the next step executes.
- FINAL.md is created by BRAND-GUARDIAN only after all steps are approved.
- Only Source marks a task as DONE in TASKMASTER.md.
