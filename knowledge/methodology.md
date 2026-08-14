# Market Research Methodology — Reference

Compact reference for the market-research skill. The full workflow lives in `SKILL.md`; this file holds the underlying methods and heuristics.

## Research formula

```text
市场数据(宏观) + 竞争分析(别人怎么赚钱) + 用户访谈(真实痛点) + 付费验证(愿不愿买) = 创业决策
```

## Evidence taxonomy

| Label | 中文 | Meaning |
|---|---|---|
| `FACT` | 确定事实 | Directly supported by a credible, attributable source |
| `INFERENCE` | 合理推测 | Reasoned from multiple facts |
| `HYPOTHESIS` | 假设 | A proposition to be tested (incl. all simulated interviews) |
| `UNKNOWN` | 未知信息 | Insufficient evidence for a responsible claim |

Simulated interviews are brainstorming only — never evidence.

## Evidence strength ladder (weakest → strongest)

```text
LLM simulation < social opinion < survey intention < interview about intention
  < interview about recent behavior < actual behavior/usage < observed purchase / paid pilot
```

## Source hierarchy

official statistics / government > first-party company pages & pricing & filings > direct customer statements (reviews, forums, interviews) > reputable research orgs > reputable journalism > expert commentary > aggregators > unattributed blogs.

## Market sizing (bottom-up)

```text
Number of reachable customers × realistic annual price × realistic penetration = serviceable revenue
```

TAM = theoretical total; SAM = serviceable for the defined offering/geography; SOM = realistically reachable in a time horizon. Never treat TAM as expected revenue.

## Competitor research

A competitor is any alternative competing for the customer's budget or attention: direct products, adjacent products, internal build, service providers, manual workflows, hiring staff, doing nothing.

The key question is not "who has the most features?" but "why would this customer change behavior?".

## Customer research

Map five roles: problem owner, user, economic buyer, decision maker, blocker.

Ask "why is the user suffering now?", not "what do they need?". Target frequent, repeated, measurable pain with an existing budget or obvious economic consequence.

## Willingness to pay (weak → strong)

stated intent < current spend < switching budget < signed pilot < paid trial < deposit < pre-order < renewal.

## Go-to-market

For each segment estimate: where prospects gather, cost to reach, contact authority, sales cycle, trust barrier, onboarding effort. A large but inaccessible market is worse than a smaller reachable niche.

## One-person company lens

Score higher: narrow scope, low onboarding, self-service acquisition, low support, high gross margin, low regulatory burden, repeatable delivery, obvious ROI. Score lower: big sales teams, field service, high-touch implementation, 24/7 ops, heavy compliance, bespoke integrations.

## Red-team method

For every optimistic conclusion, write the strongest alternative explanation and the test that would distinguish them. Watch for: temporary hype, pain already solved, large-but-inaccessible market, incumbents able to copy, buyer without budget authority.

## Validation ladder (cheapest credible experiment first)

```text
problem interview -> landing page -> qualified lead -> demo -> concierge MVP -> paid pilot -> repeatable sales -> scalable product
```

## Kill criteria

Define stop conditions before results are known, e.g. fewer than 2 of 20 qualified interviews report the target pain; <10% of qualified prospects request a demo; no paid pilot after 30 conversations; CAC exceeding contribution margin. Adjust thresholds to the business model — they are hypotheses, not universal laws.
