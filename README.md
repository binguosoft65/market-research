# Market Research Skill

Evidence-driven, executable market research methodology for AI agents. Turns a vague business idea into a traceable research project: sources, evidence ledger, competitors, customers, pricing, experiments, scoring, and a decision-quality feasibility report (可行性报告).

Works in **Claude Code, opencode, codex, hermes, zcode** and any agent that scans for `SKILL.md`.

## What it does

- Interview the user for basic context first — never answers "is there a market?" with generic praise.
- Runs a 7-step research process: research framework → industry scan → competitor analysis (most important) → real customer pain → pricing/willingness-to-pay → channel plan → sales-objection pressure test.
- Labels every claim `FACT` / `INFERENCE` / `HYPOTHESIS` / `UNKNOWN` (确定事实 / 合理推测 / 假设 / 未知信息) to prevent fabrication.
- Outputs a fixed-format feasibility report (Markdown template + JSON schema).
- Optional Python scripts provide durable storage (SQLite), scoring, and exports.

## Install (offline)

The skill is fully offline — plain Markdown + optional Python scripts. Choose one:

**A. One-command installer** (copies the skill into an agent's skills directory):

```bash
# Linux / macOS (defaults to ~/.claude/skills)
./install.sh

# or a custom target
./install.sh ~/.config/opencode/skills
```

```powershell
# Windows PowerShell (defaults to $HOME\.claude\skills)
.\install.ps1

# or a custom target
.\install.ps1 -Dest "$HOME\.config\opencode\skills"
```

**B. Manual** — copy the whole `market-research/` folder (SKILL.md + scripts + schemas + templates + knowledge) into your agent's skills directory:

| Agent | Skills directory |
|---|---|
| Claude Code | `~/.claude/skills/market-research/` |
| opencode | `~/.config/opencode/skills/market-research/` (also auto-loads `~/.claude/skills/`) |
| codex / hermes / zcode / others | wherever the tool scans for `SKILL.md` |

See `INSTALL.md` for details.

## Quick start (optional scripts)

The scripts are optional — an agent can run the whole methodology with just its web/search tools. To use them:

```bash
pip install -r requirements.txt   # only PyYAML

python scripts/init.py "AI智能客服" --mode deep --geography 中国 \
  --segment "中小企业、电商商家" --budget "10万人民币" --advantages "电商运营经验"
```

Then populate sources / evidence / competitors / customers / pricing / experiments, and generate the report:

```bash
python scripts/ingest.py --project projects/<slug> --file sources.jsonl
python scripts/evidence.py add --project projects/<slug> --claim "..." --type FACT --source SRC-0001
python scripts/competitor.py add --project projects/<slug> --file competitors.jsonl
python scripts/customer.py add --project projects/<slug> --file customers.jsonl
python scripts/pricing.py add --project projects/<slug> --file pricing.jsonl
python scripts/experiments.py add --project projects/<slug> --file experiments.jsonl
python scripts/scoring.py --project projects/<slug> --scores market_attractiveness=7 customer_pain=8 competition_intensity=8 risk=8
python scripts/report.py --project projects/<slug>
python scripts/export.py --project projects/<slug> --format json
```

## Scripts

| Script | Purpose |
|---|---|
| `scripts/init.py` | Create a project (folders, `research.yaml`, SQLite DB) |
| `scripts/ingest.py` | Import sources from JSONL |
| `scripts/evidence.py` | Add/list evidence records |
| `scripts/competitor.py` | Import/list competitors |
| `scripts/customer.py` | Import/list customer segments |
| `scripts/pricing.py` | Import/list pricing & unit economics |
| `scripts/experiments.py` | Import/list/update validation experiments |
| `scripts/scoring.py` | Weighted opportunity score (0-10) |
| `scripts/report.py` | Generate the final markdown report |
| `scripts/export.py` | Export all tables to JSON or CSV |

Scoring note: `competition_intensity` and `risk` are reverse-scored — enter 10 for the worst case; `scoring.py` inverts them automatically.

## Report format

The final deliverable is a fixed-format **可行性报告 (feasibility report)** — see `templates/final-report.md` (the canonical structure) and `schemas/report.json` (the machine-readable version). Decision must be one of `GO / CONDITIONAL GO / NO-GO`.

## License

MIT — see `LICENSE`.
