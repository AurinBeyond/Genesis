#!/usr/bin/env bash
set -euo pipefail

echo "→ Starting structure normalization..."

# Ensure required folders exist
mkdir -p logs
mkdir -p archive
mkdir -p agents/templates
mkdir -p agents/course-creator

# Ensure archive is tracked by Git
touch archive/.gitkeep

# Move loose log file into logs/
if [[ -f "updates.log" ]]; then
  mv -n updates.log logs/updates.log
  echo "Moved updates.log → logs/"
fi

# Move agent-related root files into agents/
for file in AGENT.md AGENTS.md AGENTS-CONFIG.md AGENTS-CONFIG.v.2.md; do
  if [[ -f "$file" ]]; then
    mv -n "$file" agents/
    echo "Moved $file → agents/"
  fi
done

# NOTE:
# laws/ EI LIIGUTATA automaatselt
# (väldime olemasoleva loogika rikkumist)

# Ensure logs core files exist
touch logs/runtime.log
touch logs/research.log

# Ensure state.json exists
if [[ ! -f "logs/state.json" ]]; then
cat > logs/state.json <<EOF
{
  "system": "GENESIS",
  "status": "active",
  "last_run": null
}
EOF
echo "Created logs/state.json"
fi

echo "✓ Structure normalized safely"
echo "run at $(date -u)" >> logs/runtime.log
