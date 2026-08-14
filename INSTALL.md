# Installing the market-research skill

The skill is fully **offline**: a plain `SKILL.md` (read by the agent) plus optional Python scripts (durable storage, scoring, exports). The only Python dependency is PyYAML, and only if you use the scripts.

## Method A — installer script

```bash
# Linux / macOS
./install.sh [target-dir]

# Windows PowerShell
.\install.ps1 [-Dest target-dir]
```

Both default to `~/.claude/skills` (a directory auto-loaded by both Claude Code and opencode). Pass a different directory to target a specific agent.

## Method B — manual copy

Copy the whole `market-research/` folder (not just `SKILL.md`, so templates and scripts are available) into the agent's skills directory:

| Agent | Location |
|---|---|
| Claude Code | `~/.claude/skills/market-research/` |
| opencode | `~/.config/opencode/skills/market-research/` (also auto-loads `~/.claude/skills/` and `~/.agents/skills/`) |
| codex (OpenAI) | the directory scanned for `SKILL.md` / agents, e.g. `~/.codex/skills/market-research/` |
| hermes / zcode / others | wherever the tool scans for `SKILL.md` |

After copying, **restart the agent** so it re-scans and loads the skill.

## Requirements (scripts only)

- Python 3.9+
- `pip install -r requirements.txt` (only PyYAML)

The skill body itself has no runtime dependencies.

## Project layout

```text
market-research/
├── SKILL.md           # the skill (loaded by the agent)
├── README.md
├── INSTALL.md
├── LICENSE
├── requirements.txt
├── install.sh / install.ps1
├── scripts/           # optional Python automation
├── schemas/           # JSON schemas (sources/evidence/.../report)
├── templates/         # working briefs + the canonical report format
└── knowledge/         # methodology reference
```

Projects (runtime data) are created under `projects/<slug>/` by `scripts/init.py` and are not part of the skill itself.
