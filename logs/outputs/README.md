# logs/outputs/

This directory stores agent outputs awaiting Source review.

## Naming convention
Each output file is named after its Task ID:
  TASK-001.md, TASK-002.md, etc.

## Rules
- Agent writes output here after execution.
- Agent must NOT overwrite an existing file.
- Source reviews and approves before the output is used.
- Only Source marks a task as DONE in TASKMASTER.md.
