#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone

from common import connect, load_jsonl_or_json

EXPERIMENT_FIELDS = [
    'name', 'hypothesis', 'target_segment', 'action', 'metric', 'threshold',
    'deadline', 'kill_criteria', 'status', 'result',
]


def add_experiments(project, path):
    rows = load_jsonl_or_json(path)
    con = connect(project)
    now = datetime.now(timezone.utc).isoformat()
    for i, x in enumerate(rows, 1):
        eid = x.get('id') or f'EXP-{i:04d}'
        values = [x.get(f) for f in EXPERIMENT_FIELDS]
        con.execute(
            'INSERT OR REPLACE INTO experiments(id, name, hypothesis, target_segment, '
            'action, metric, threshold, deadline, kill_criteria, status, result, '
            'created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
            (eid, *values, now),
        )
    con.commit()
    con.close()
    print(f'imported {len(rows)} experiments')


def list_experiments(project):
    con = connect(project)
    rows = con.execute(
        'SELECT id, name, status, metric, threshold, deadline FROM experiments ORDER BY id'
    ).fetchall()
    con.close()
    for r in rows:
        print('\t'.join(map(str, r)))


def update_experiment(project, eid, status, result):
    con = connect(project)
    cur = con.execute('SELECT id FROM experiments WHERE id = ?', (eid,))
    if cur.fetchone() is None:
        con.close()
        print(f'experiment {eid} not found')
        return
    con.execute(
        'UPDATE experiments SET status = COALESCE(?, status), result = COALESCE(?, result) '
        'WHERE id = ?',
        (status, result, eid),
    )
    con.commit()
    con.close()
    print(f'updated {eid}')


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('add')
    a.add_argument('--project', required=True)
    a.add_argument('--file', required=True)

    l = sub.add_parser('list')
    l.add_argument('--project', required=True)

    u = sub.add_parser('update')
    u.add_argument('--project', required=True)
    u.add_argument('--id', required=True)
    u.add_argument('--status', choices=['planned', 'running', 'completed', 'killed'])
    u.add_argument('--result')

    args = p.parse_args()

    if args.cmd == 'add':
        add_experiments(args.project, args.file)
    elif args.cmd == 'list':
        list_experiments(args.project)
    else:
        update_experiment(args.project, args.id, args.status, args.result)


if __name__ == '__main__':
    main()
