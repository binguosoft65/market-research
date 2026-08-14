#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone

from common import connect, load_jsonl_or_json

CUSTOMER_FIELDS = [
    'segment', 'persona', 'role', 'problem', 'current_solution',
    'pain_score', 'urgency_score', 'budget_score', 'buying_trigger',
    'blockers', 'source_id', 'notes',
]


def add_customers(project, path):
    rows = load_jsonl_or_json(path)
    con = connect(project)
    now = datetime.now(timezone.utc).isoformat()
    for i, x in enumerate(rows, 1):
        cid = x.get('id') or f'CUST-{i:04d}'
        values = [x.get(f) for f in CUSTOMER_FIELDS]
        con.execute(
            'INSERT OR REPLACE INTO customers(id, segment, persona, role, problem, '
            'current_solution, pain_score, urgency_score, budget_score, buying_trigger, '
            'blockers, source_id, notes, created_at) '
            'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (cid, *values, now),
        )
    con.commit()
    con.close()
    print(f'imported {len(rows)} customers')


def list_customers(project):
    con = connect(project)
    rows = con.execute(
        'SELECT id, segment, persona, role, pain_score, urgency_score, budget_score '
        'FROM customers ORDER BY pain_score DESC'
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
        add_customers(args.project, args.file)
    else:
        list_customers(args.project)


if __name__ == '__main__':
    main()
