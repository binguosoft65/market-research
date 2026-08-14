#!/usr/bin/env bash
# Offline installer for the market-research skill.
# Copies the skill (SKILL.md + scripts + schemas + templates + knowledge)
# into an agent's skills directory.
#
# Usage:
#   ./install.sh                 # -> $HOME/.claude/skills/market-research
#   ./install.sh /target/dir     # -> /target/dir/market-research
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="market-research"
DEST="${1:-$HOME/.claude/skills}"
TARGET="$DEST/$NAME"

if [ -e "$TARGET" ]; then
  rm -rf "$TARGET"
fi
mkdir -p "$TARGET"

cp -R "$SRC/SKILL.md" "$SRC/README.md" "$SRC/INSTALL.md" "$SRC/LICENSE" \
      "$SRC/requirements.txt" "$SRC/scripts" "$SRC/schemas" \
      "$SRC/templates" "$SRC/knowledge" "$TARGET/"

echo "Installed market-research -> $TARGET"
