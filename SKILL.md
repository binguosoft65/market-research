---
name: market-research
version: 3.0.0
description: Evidence-driven market research for AI agents. Use when the user asks to evaluate a market, business idea, product opportunity, niche, competitor, customer pain, pricing/willingness-to-pay, or go-to-market plan (市场调查 / 市场研究 / 竞品分析 / 机会评估 / 用户痛点 / 付费验证). Turns a vague idea into a traceable research project with sources, evidence, competitors, customers, pricing, experiments, scoring and a decision report. Never answers "is there a market?" with generic praise — it designs and runs a real research process first.
---

# Market Research Skill

## 1. What this skill is

A reusable, evidence-driven market research methodology for AI agents. It turns a business idea into a traceable research project: sources, evidence ledger, competitors, customers, pricing, experiments, scoring, and a final decision report.

Use it for practical entrepreneurial decisions, especially:

- one-person companies
- SaaS and AI products
- developer tools
- B2B software
- AI agents
- creator/education products
- vertical software
- emerging technology markets

The objective is **not** to produce a persuasive report. The objective is to produce a **decision-quality evidence base** and a falsifiable recommendation.

## 2. What NOT to do (anti-patterns)

**Never answer a vague market question with generic praise.** Examples of the anti-pattern:

> 用户：我想做 AI 客服，有市场吗？
> ❌ 错误回答：AI 客服市场巨大，未来增长快速……

That answer has no evidence, no decision value, and no falsifiability.

Instead, the agent must **redirect the user into the research process**: interview for basic context (Step 0), then design a research framework and execute it step by step.

Other hard rules:

- **Do not give conclusions before designing the research.** First deliver the research framework (the "调研目录"), then gather evidence.
- **Do not fabricate.** No invented interviews, revenue figures, market sizes, or competitor data. Simulated interviews are HYPOTHESIS-generation only, never presented as real evidence.
- **Do not answer "how big is the market?" with a headline number.** Show TAM/SAM/SOM with assumptions and formulas, bottom-up.
- **Do not average contradictory sources blindly.** Preserve both, explain the difference.

## 3. Core principles

1. **Evidence before conclusion.** Important claims must point to source evidence.
2. **Separate certainty levels.** Label every claim `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN` (see §15). In Chinese: 确定事实 / 合理推测 / 假设 / 未知信息.
3. **Competition before market.** For early-stage ideas, research the competition *first* — the real competitor is often an existing workflow, spreadsheet, employee, agency, or "doing nothing", not just rival products.
4. **Pain, not needs.** Ask "why is the user suffering *right now*?", not "what does the user need?". Look for frequent, repeated, measurable pain with an existing budget or obvious economic consequence.
5. **Search for disconfirmation.** Every positive claim should have at least one attempt to find contrary evidence.
6. **"User says they need it" ≠ "user will pay".** Treat stated intent as weak evidence; validate with willingness-to-pay tests.
7. **Quantify assumptions.** Market size, conversion, CAC, price, margins, and demand must show assumptions and formulas.
8. **Prefer current, first-party, direct sources.** Company docs, pricing pages, filings, official statistics, customer reviews, direct user discussions.
9. **Triangulate.** Major conclusions should be supported by multiple independent sources.
10. **Optimize for action.** End with experiments, thresholds, and kill criteria — not a nice-looking document.

## 4. The research formula

```text
市场数据(宏观) + 竞争分析(别人怎么赚钱) + 用户访谈(真实痛点) + 付费验证(愿不愿买) = 创业决策
```

A helpful agent does the first three stages with strong sourcing discipline, and pushes the last stage toward real signals (reviews, forums, interviews, small paid tests) instead of relying on simulated opinion.

## 5. Research lifecycle

```text
Idea
  -> Interview (basic context)
  -> Research framework (调研目录)
  -> Industry scan (宏观)
  -> Competitor analysis (竞争 — most important)
  -> Customer pain analysis (真实痛点)
  -> Pricing / willingness-to-pay validation
  -> Channel & acquisition plan
  -> Sales objection pressure test (red-team)
  -> Opportunity scoring
  -> Validation experiments
  -> Decision (GO / CONDITIONAL GO / NO-GO + kill criteria)
```

An agent may skip a stage only when it explicitly records why.

## 6. Modes

### Quick Scan
Early idea screening. Target 10–20 high-quality sources and a 1–3 page conclusion.

### Deep Research
Investment, product strategy, or major startup decision. Broad triangulation, primary/secondary sources, competitor depth, user evidence, pricing evidence, explicit uncertainty.

### Validation Mode
After an opportunity looks promising. Focus on customer interviews, landing pages, presales, pilot projects, usage tests, and other real-world experiments.

## 7. Workflow — Step 0: interview the user first

Before any research, **ask the user to fill in basic context**. If not already supplied, guide them with this template (one question at a time or the whole form):

```text
创业想法：[一句话描述你的产品/机会]

目标用户：[谁最需要它？谁付钱？]

地区：[目标市场/国家/城市]

预算：[可投入的资金/时间范围，或定价假设]

我的优势：[你/团队的独特资源、经验、渠道]
```

| 字段 | 用途 | 对应脚本参数 |
|---|---|---|
| 创业想法 | 项目名 + 决策上下文 | `name` |
| 目标用户 | 目标客群，用于竞品/客户分析 | `--segment` |
| 地区 | 研究地理范围 | `--geography` |
| 预算 | 定价/单位经济假设、可行性 | `--budget` |
| 我的优势 | 创始人/一人公司适配度、护城河 | `--advantages` |

Blank fields use a sensible default and are marked `UNKNOWN` — never invented. If 创业想法、目标用户 or 预算 is missing, ask a clarifying follow-up first.

## 8. Workflow — Step 1: define the research framework (先设计研究方法，不给结论)

Do **not** jump to conclusions. First deliver a research framework — the "调研目录" — covering:

1. 市场规模 (market size)
2. 用户画像 (customer profile)
3. 用户痛点 (pain points)
4. 当前解决方案 (current alternatives)
5. 竞争对手 (competitors)
6. 用户付费意愿 (willingness to pay)
7. 获客渠道 (acquisition channels)
8. 创业机会窗口 (opportunity window)
9. 风险分析 (risks)

For each, state the **method** (which sources, which questions) and the **time window** (e.g. 2024–2026). Write this as the working brief using `templates/research-plan.md`.

## 9. Workflow — Step 2: industry scan (宏观)

Research the market macro before diving into a niche. For each analysis area (市场规模, 增长趋势, 主要玩家, 商业模式, 技术趋势, 投融资情况):

- Require a **source for every material number** (URL + date).
- State the **time window** and **geography**.
- Label every claim `FACT` / `INFERENCE` / `HYPOTHESIS` / `UNKNOWN` — this is what stops the model from "making up stories".
- Record sources with `scripts/ingest.py`, claims with `scripts/evidence.py`.

## 10. Workflow — Step 3: competitor analysis (最重要)

For early-stage ideas, **research competition before market**. List head players *and* substitutes (manual labor, spreadsheets, agencies, internal tools, legacy software, doing nothing).

For each competitor, analyze:

1. 产品定位 (positioning)
2. 目标客户 (target customer)
3. 收费模式 (pricing/business model)
4. 优势 (strengths)
5. 劣势 (weaknesses)
6. 用户评价 (user signals/reviews)
7. 我作为创业者如何避开竞争 (how to differentiate)

Produce a comparison table:

| 公司 | 客户 | 价格 | 优势 | 弱点 |
|---|---|---|---|---|
| 腾讯企点 | 大企业 | 高 | 生态 | 复杂 |
| Chatwoot | 技术团队 | 低 | 开源 | 中文生态弱 |

Then explicitly name the **market gap**: underserved segment, unsolved pain, distribution gap, pricing gap, workflow gap. Use `templates/competitor-analysis.md` and import with `scripts/competitor.py`.

## 11. Workflow — Step 4: analyze real customer pain (最关键)

Do **not** ask "用户需要什么？". Ask "用户现在为什么痛苦？".

Generate candidate pain points with **simulated interviews** (e.g. 100 fictional merchants), each answering:

1. 当前客服方式 (current solution)
2. 每月客服成本 (monthly cost)
3. 最大痛点 (biggest pain)
4. 为什么不购买现有产品 (why not buy existing solutions)
5. 什么价格愿意购买 (acceptable price)
6. 最希望解决的问题 (most-desired outcome)

Then **cluster** the results into pain clusters, e.g.:

- 人工客服工资太高
- 夜间没人回复
- AI 不理解商品
- 平台违规风险

**Critical rule:** simulated interviews are `HYPOTHESIS` only. Every pain cluster must then be **validated with real evidence** — scrape/read 淘宝/抖音/小红书 comments, 知乎/Reddit/forum threads, app-store reviews, or run real interviews — before it becomes `FACT`. Record validated pain as customer records via `scripts/customer.py`.

## 12. Workflow — Step 5: validate willingness to pay (付费验证)

"用户说需要 ≠ 用户付钱". Based on the validated pain points, design **multiple pricing plans** (e.g. 99元/月基础, 399元/月+销售机器人, 按成交收费), and analyze:

- which plan converts easiest and why
- what evidence would confirm willingness to pay (existing spend, switching budget, deposit, pre-order, paid pilot, renewal)

Use `templates/pricing-analysis.md`, record assumptions with `scripts/pricing.py`, and always express unit economics with formulas.

## 13. Workflow — Step 6: channel & acquisition plan

Many startups fail on acquisition, not product. For the target segment, analyze:

1. 客户在哪里聚集 (where prospects gather)
2. 最低成本获客渠道 (cheapest acquisition channels)
3. 内容营销方案 (content marketing)
4. 私域打法 (private-domain/community play)
5. 销售流程 (sales process)

Deliver a **100-day acquisition plan** with measurable milestones. Use `templates/channel-plan.md`.

## 14. Workflow — Step 7: sales objection pressure test (red-team)

Before recommending "proceed", attack the thesis. Two techniques:

**A. Simulated sales objections.** The agent plays a skeptical buyer who keeps rejecting until convinced:

- 太贵
- 我已有客服
- AI 不好用
- 怕泄露数据
- 没有效果

**B. Red-team the thesis.** Ask:

- What evidence would make the thesis wrong?
- Which assumption has the largest uncertainty?
- Could the market be large but inaccessible?
- Is the pain real but already solved adequately?
- Can incumbents copy the core feature?
- Does the buyer have budget authority?
- Can this be delivered profitably by one person?
- Are current signals caused by temporary hype?

Use `templates/sales-objection.md`. Record unresolved risks.

## 15. Evidence taxonomy

Map every important claim to a certainty level. This is the anti-fabrication mechanism.

| Label | 中文 | Meaning |
|---|---|---|
| `FACT` | 确定事实 | Directly supported by a credible, attributable source |
| `INFERENCE` | 合理推测 | Reasoned from multiple facts |
| `HYPOTHESIS` | 假设 | A proposition to be tested; includes all simulated interviews |
| `UNKNOWN` | 未知信息 | Insufficient evidence for a responsible claim |

Rules:

- A claim is **Decision-grade** only when it is specific, recent enough, attributable, reproducible, relevant to the segment, and supported by direct evidence.
- When sources disagree: preserve both, check date/geography/definitions/methodology, explain the difference, and do not average blindly.

## 16. Source hierarchy & quality

Prefer, roughly in order:

1. official statistics / government / regulatory data
2. first-party company pages, pricing, filings, product docs
3. direct customer/user statements (reviews, forums, interviews)
4. reputable research organizations
5. reputable journalism
6. expert commentary
7. aggregators and directories
8. unattributed blog posts

A lower-tier source can still be useful when it contains unique primary evidence — but the report must say so.

## 17. Agent pipeline (multi-agent orchestration)

When orchestration is available (sub-agents / multi-step runs), structure the work as a pipeline. Each stage consumes the previous stage's output:

```text
输入：创业想法
  -> 行业研究 (industry scan)
  -> 竞争分析 (competitor analysis)
  -> 用户画像 (customer profile)
  -> 痛点分析 (pain analysis)
  -> 商业模式 (business model / pricing)
  -> 投资评估 (investment/opportunity assessment)
  -> 输出：创业可行性报告 (feasibility report)
```

A single agent can run the same stages sequentially if no sub-agent runner exists.

## 18. Small-niche playbook (one-person company)

Do not research "AI 市场大不大". Research **small cuts**. For example:

- "给制造企业老板做 AI 销售员" → 工厂老板有没有销售压力？是否愿意让数字人介绍产品？一个订单价值多少？ROI 多少？
- "AI 课程制作工具" → 培训机构制作课程成本？老师愿不愿用 AI 生成课件？是否愿每月付费？
- "AI 客服 + 销售机器人" → 电商老板每月客服成本？AI 能否替代 1 个人？节省多少钱？

Score one-person fit higher when the product has: narrow scope, low onboarding complexity, self-service acquisition, low support burden, high gross margin, low regulatory burden, repeatable delivery, obvious ROI. Score lower for: large sales teams, field service, high-touch implementation, 24/7 operations, heavy compliance, bespoke enterprise integrations.

## 19. Project layout & CLI reference

```text
market-research-skill/
├── SKILL.md
├── scripts/
├── schemas/
├── templates/
└── knowledge/

projects/<slug>/
├── research.yaml
├── market-research.db
├── sources/
├── evidence/
├── competitors/
├── customers/
├── pricing/
├── experiments/
├── reports/
└── exports/
```

The Python scripts create and maintain the SQLite database. They are **optional**: an agent can run the whole methodology with only its web/search tools and markdown notes. When used:

```bash
# Step 0-1: create project with the interview answers
python scripts/init.py "AI智能客服" --mode deep --geography 中国 \
  --segment "中小企业、电商商家" --budget "10万人民币" --advantages "电商运营经验"

# Step 2: ingest sources
python scripts/ingest.py --project projects/<slug> --file sources.jsonl

# Record evidence (label FACT/INFERENCE/HYPOTHESIS/UNKNOWN)
python scripts/evidence.py add --project projects/<slug> --claim "..." --type FACT --source SRC-0001 --text "..."
python scripts/evidence.py list --project projects/<slug>

# Step 3: competitors
python scripts/competitor.py add --project projects/<slug> --file competitors.jsonl
python scripts/competitor.py list --project projects/<slug>

# Step 4: customers
python scripts/customer.py add --project projects/<slug> --file customers.jsonl

# Step 5: pricing / unit economics
python scripts/pricing.py add --project projects/<slug> --file pricing.jsonl

# Experiments & decision
python scripts/experiments.py add --project projects/<slug> --file experiments.jsonl
python scripts/scoring.py --project projects/<slug> --scores market_attractiveness=7 customer_pain=8 competition_intensity=8 risk=8
python scripts/report.py --project projects/<slug>

# Export
python scripts/export.py --project projects/<slug> --format json
python scripts/export.py --project projects/<slug> --format csv
```

Scoring note: `competition_intensity` and `risk` are reverse-scored — enter 10 for the worst case; `scoring.py` inverts them automatically.

## 20. Final report: canonical format

The final deliverable is a **可行性报告 (feasibility report)**. Its format is fixed and defined in `templates/final-report.md` — that file is the single source of truth for the output structure. A machine-readable JSON version follows `schemas/report.json`.

Format rules (mandatory):

- **Section order and titles are fixed.** Do not add or remove core sections (an "Appendix" may be added).
- **决策建议只能取三个值之一：** `GO` / `CONDITIONAL GO` / `NO-GO`. 置信度只能取 `LOW` / `MEDIUM` / `HIGH`.
- **Every material quantitative claim must carry a source ID** (`SRC-xxxx` / `EVD-xxxx`).
- **Unfilled fields must be marked `UNKNOWN`** — never invented.
- The report must answer all ten questions:

1. Is the problem real? (with evidence)
2. Who urgently cares? (who experiences / uses / decides / pays / blocks)
3. What do they use today? (current alternative — the real competitor)
4. Who are the competitors and substitutes? (table)
5. Why would anyone switch? (the gap)
6. What are they willing to pay? (pricing validation)
7. How can customers be acquired? (channel + 100-day plan)
8. What did the sales objection test reveal? (red-team)
9. What remains unknown? (UNKNOWN items)
10. What is the smallest validation experiment? + kill criteria

The fifteen canonical sections are: 报告元信息, 项目简报, 执行决策, 结论摘要, 市场分析, 客户与痛点, 竞争分析, 商业模式与定价, 获客渠道, 销售压力测试与红队, 证据台账, 评分卡, 验证实验与放弃标准, 最终建议, 来源附录.

## 21. Cross-agent usage

This skill is a plain Markdown file with standard `name` + `description` frontmatter, so it works in any agent that scans for `SKILL.md`. Install by copying the `market-research/` folder into that tool's skills directory (or pointing the tool's config at this path):

- **Claude Code**: `~/.claude/skills/market-research/SKILL.md`
- **opencode**: `~/.config/opencode/skills/market-research/SKILL.md` (also auto-loads `~/.claude/skills/` and `~/.agents/skills/`)
- **codex / hermes / zcode / others**: wherever the tool scans for `SKILL.md` (copy the whole `market-research/` folder, not just `SKILL.md`, so the templates and scripts are available)

The Python scripts are optional; they require Python 3.9+ and PyYAML (`pip install -r requirements.txt`). Everything else is pure Markdown instructions.

## 22. What this skill does not do

- It does not guarantee that a business will succeed.
- It does not fabricate customer interviews, revenue figures, market sizes, or competitor data.
- It does not treat LLM-generated opinions or simulated interviews as market evidence.
- It does not replace legal, financial, regulatory, or investment due diligence.
