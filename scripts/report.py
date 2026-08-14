#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
from pathlib import Path

from common import REVERSE_SCORED, connect


def fmt(v):
    if v is None:
        return '—'
    if isinstance(v, float):
        return f'{v:.2f}'
    return str(v)


def build_report(project):
    root = Path(project)
    con = connect(root)

    meta = dict(con.execute('SELECT key, value FROM meta'))
    sources = con.execute(
        'SELECT id, title, url, source_type, published_at, credibility FROM sources '
        'ORDER BY credibility DESC'
    ).fetchall()
    evidence = con.execute(
        'SELECT id, evidence_type, claim, source_id, confidence, counterevidence FROM evidence '
        'ORDER BY id'
    ).fetchall()
    comps = con.execute(
        'SELECT id, name, category, target_customer, business_model, pricing, threat_level '
        'FROM competitors ORDER BY threat_level DESC'
    ).fetchall()
    customers = con.execute(
        'SELECT id, segment, persona, role, problem, current_solution, pain_score, '
        'urgency_score, budget_score FROM customers ORDER BY pain_score DESC'
    ).fetchall()
    pricing = con.execute(
        'SELECT id, segment, price, currency, price_unit, arpu, gross_margin, '
        'implementation_cost, support_cost, sales_cycle_days, conversion_rate, cac, '
        'payback_months, retention_months, break_even_customers FROM pricing ORDER BY id'
    ).fetchall()
    experiments = con.execute(
        'SELECT id, name, hypothesis, target_segment, action, metric, threshold, deadline, '
        'kill_criteria, status, result FROM experiments ORDER BY id'
    ).fetchall()
    scores = con.execute(
        'SELECT dimension, score, weight, rationale FROM scores ORDER BY dimension'
    ).fetchall()
    con.close()

    score = sum((10 - s) * w if d in REVERSE_SCORED else s * w for d, s, w, _ in scores)

    name = meta.get('project_name', 'Untitled')
    lines = [f'# 可行性报告：{name}', '']

    # 1. 报告元信息
    lines += ['## 报告元信息', '']
    lines += ['| 字段 | 值 |', '|---|---|']
    lines.append(f'| 项目名 | {name} |')
    lines.append(f'| 生成时间 | {datetime.now(timezone.utc).isoformat()}Z |')
    lines.append(f'| 研究模式 | {meta.get("mode", "—")} |')
    lines.append(f'| 时间范围 | _待补充_ |')
    lines.append(f'| 地区 | {meta.get("geography") or "—"} |')
    lines.append('')

    # 2. 项目简报
    lines += ['## 一、项目简报', '']
    brief = [
        ('创业想法', name),
        ('目标用户', meta.get('target_segment')),
        ('地区', meta.get('geography')),
        ('预算', meta.get('budget')),
        ('我的优势', meta.get('founder_advantages')),
    ]
    for k, v in brief:
        if v:
            lines.append(f'- **{k}:** {v}')
    lines.append('')

    # 3. 执行决策
    lines += ['## 二、执行决策', '']
    lines += ['| 字段 | 值 |', '|---|---|']
    lines.append('| 建议 | **CONDITIONAL GO** _(待定：GO / CONDITIONAL GO / NO-GO)_ |')
    lines.append(f'| 机会评分 | {score:.2f} / 10 |')
    lines.append('| 置信度 | _(待定：LOW / MEDIUM / HIGH)_ |')
    lines.append('| 一句话决策依据 | _待补充_ |')
    lines.append('')

    # 4. 结论摘要
    lines += ['## 三、结论摘要', '']
    lines += ['### 为什么可能成功', '', '_待补充_', '',
              '### 为什么可能失败', '', '_待补充_', '',
              '### 最大的未知', '', '_待补充_', '']

    # 5. 市场分析
    lines += ['## 四、市场分析（行业扫描）', '']
    lines += ['### 市场定义与时间范围', '', '_待补充_', '',
              '### 市场规模（自下而上，含公式）', '',
              '| 层级 | 估算 | 公式与假设 |', '|---|---|---|',
              '| TAM | _待补充_ | |', '| SAM | _待补充_ | |', '| SOM | _待补充_ | |', '',
              '### 增长趋势', '', '_待补充_', '',
              '### 主要玩家与商业模式', '', '_待补充_', '',
              '### 投融资情况', '', '_待补充_', '']

    # 6. 客户与痛点
    lines += ['## 五、客户与痛点', '']
    if customers:
        lines += ['| ID | 客群 | 画像 | 角色 | 痛点 | 当前方案 | 痛感 | 紧迫 | 预算 |',
                  '|---|---|---|---|---|---|---:|---:|---:|']
        for c in customers:
            lines.append(f'| {c[0]} | {c[1]} | {c[2] or "—"} | {c[3] or "—"} | {c[4] or "—"} | {c[5] or "—"} | {fmt(c[6])} | {fmt(c[7])} | {fmt(c[8])} |')
    else:
        lines.append('_无客户记录。_')
    lines.append('')

    # 7. 竞争分析
    lines += ['## 六、竞争分析', '']
    if comps:
        lines += ['| ID | 公司 | 类型 | 客户 | 商业模式 | 价格 | 威胁度 |',
                  '|---|---|---|---|---|---|---:|']
        for c in comps:
            lines.append(f'| {c[0]} | {c[1]} | {c[2] or "—"} | {c[3] or "—"} | {c[4] or "—"} | {c[5] or "—"} | {fmt(c[6])} |')
    else:
        lines.append('_无竞品记录。_')
    lines.append('')
    lines += ['### 替代品', '', '_待补充_', '', '### 市场空白 / 切入点', '', '_待补充_', '']

    # 8. 商业模式与定价
    lines += ['## 七、商业模式与定价', '']
    if pricing:
        lines += ['| 客群 | 价格 | ARPU | 毛利率 | CAC | 回本(月) | 留存(月) | 盈亏平衡 |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|']
        for p in pricing:
            price = f'{fmt(p[2])} {p[3] or ""}/{p[4] or "unit"}'.strip()
            lines.append(f'| {p[1]} | {price} | {fmt(p[5])} | {fmt(p[6])} | {fmt(p[11])} | {fmt(p[12])} | {fmt(p[13])} | {fmt(p[14])} |')
    else:
        lines.append('_无定价记录。_')
    lines.append('')
    lines += ['### 最易成交方案与理由', '', '_待补充_', '', '### 付费意愿证据', '', '_待补充_', '']

    # 9. 获客渠道
    lines += ['## 八、获客渠道', '']
    lines += ['### 客户聚集地', '', '_待补充_', '',
              '### 最低成本渠道', '', '_待补充_', '',
              '### 100 天获客计划', '', '_待补充_', '']

    # 10. 销售压力测试与红队
    lines += ['## 九、销售压力测试与红队', '']
    counter = [e for e in evidence if e[5]]
    if counter:
        lines += ['### 反证记录', '']
        for e in counter:
            lines.append(f'- **{e[0]} [{e[1]}]** {e[2]} — 反证: {e[5]}')
        lines.append('')
    lines += ['### 最强异议与回应', '', '_待补充_', '', '### 处于风险中的关键假设', '', '_待补充_', '']

    # 11. 证据台账
    lines += ['## 十、证据台账', '']
    if evidence:
        lines += ['| ID | 类型 | 主张 | 来源 | 置信度 |', '|---|---|---|---|---:|']
        for e in evidence:
            lines.append(f'| {e[0]} | {e[1]} | {e[2]} | {e[3] or "none"} | {fmt(e[4])} |')
    else:
        lines.append('_无证据记录。_')
    lines.append('')

    # 12. 评分卡
    lines += ['## 十一、评分卡', '', '| 维度 | 得分 | 权重 | 有效分 | 理由 |',
              '|---|---:|---:|---:|---|']
    for d, s, w, r in scores:
        eff = (10 - s) if d in REVERSE_SCORED else s
        rev = ' (反向)' if d in REVERSE_SCORED else ''
        lines.append(f'| {d}{rev} | {s:.1f} | {w:.2f} | {eff:.1f} | {r} |')
    lines.append('')

    # 13. 验证实验与放弃标准
    lines += ['## 十二、验证实验与放弃标准', '']
    if experiments:
        lines += ['| ID | 实验 | 状态 | 假设 | 指标 | 阈值 | 截止 | 放弃标准 |',
                  '|---|---|---|---|---|---|---|---|']
        for x in experiments:
            lines.append(f'| {x[0]} | {x[1]} | {x[9] or "planned"} | {x[2] or "—"} | {x[5] or "—"} | {x[6] or "—"} | {x[7] or "—"} | {x[8] or "—"} |')
    else:
        lines.append('_无验证实验。_')
    lines.append('')

    # 14. 最终建议
    lines += ['## 十三、最终建议', '']
    lines += ['- **下一步做什么：** _待补充_', '- **现在不该做什么：** _待补充_', '- **能改变决策的最小测试：** _待补充_', '']

    # 15. 来源附录
    lines += ['## 十四、来源附录', '']
    if sources:
        lines += ['| ID | 标题 | URL | 类型 | 日期 | 可信度 |', '|---|---|---|---|---|---|']
        for s in sources:
            lines.append(f'| {s[0]} | [{s[1]}]({s[2]}) | {s[3] or "—"} | {s[4] or "—"} | {fmt(s[5])} |')
    else:
        lines.append('_无来源记录。_')
    lines.append('')

    out = root / 'reports' / 'final-report.md'
    out.parent.mkdir(exist_ok=True)
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return out, score


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--project', required=True)
    args = p.parse_args()
    out, score = build_report(args.project)
    print(f'{out} (score {score:.2f}/10)')


if __name__ == '__main__':
    main()
