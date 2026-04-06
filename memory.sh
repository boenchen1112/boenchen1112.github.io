#!/usr/bin/env bash
# memory.sh — launch Claude with project memory as system prompt

PRIMER=$(cat "C:/Users/user/.claude/primer.md" 2>/dev/null || echo "(primer.md not found)")
COMMITS=$(git log --oneline -5 2>/dev/null || echo "(no git history)")
BRANCH=$(git branch --show-current 2>/dev/null || echo "(unknown)")
MODIFIED=$(git status --short 2>/dev/null || echo "(no git status)")
LESSONS=$(cat "tasks/lessons.md" 2>/dev/null || echo "(lessons.md not found)")

SYSTEM_PROMPT="## Primer
$PRIMER

## Git Context
Branch: $BRANCH

Last 5 commits:
$COMMITS

Modified files:
$MODIFIED

## Lessons Learned
$LESSONS"

claude \
  --permission-mode acceptEdits \
  --allowedTools "Bash(git:*) Bash(npm:*) Edit Write Read" \
  --system-prompt "$SYSTEM_PROMPT"
