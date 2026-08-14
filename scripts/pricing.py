#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone

from common import connect, load_jsonl_or_json

PRICING_FIELDS = [
    'segment', 'price', 'currency', 'price_unit', 'arpu', 'gross_margin',
    'implementation_cost', 'support_cost', 'sales_cycle_days', 'conversion_rate',
    'cac', 'payback_months', 'retention_months', 'break_even_customers', 'notes',
]


def add_pricing(project, path):
    rows = load_jsonl_or_json(path)
    con = connect(project)
    now = datetime.now(timezone.utc).isoformat()
    for i, x in enumerate(rows, 1):
        pid = x.get('id') or f'PRC-{i:04d}'
        values = [x.get(f) for f in PRICING_FIELDS]
        con.execute(
            'INSERT OR REPLACE INTO pricing(id, segment, price, currency, price_unit, '
            'arpu, gross_margin, implementation_cost, support_cost, sales_cycle_days, '
            'conversion_rate, cac, payback_months, retention_months, '
            'break_even_customers, notes, created_at) '
            'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (pid, *values, now),
        )
    con.commit()
    con.close()
    print(f'imported {len(rows)} pricing rows')


def list_pricing(project):
    con = connect(project)
    rows = con.execute(
        'SELECT id, segment, price, currency, arpu, gross_margin, cac, payback_months '
        'FROM pricing ORDER BY id'
    ).fetchall()
    con.close()
    for r in rows:
        print('\t'.join(map(str, r)))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('add')
    a.add_argument('--project', required=True)
    a.add_argument('--file', required=True)
    l = sub.add_parser('list')
    l.add_argument('--project', required=True)
    args = p.parse_args()

    if args.cmd == 'add':
        add_pricing(args.project, args.file)
    else:
        list_pricing(args.project)


if __name__ == '__main__':
    main()
