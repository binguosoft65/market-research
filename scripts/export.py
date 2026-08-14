#!/usr/bin/env python3
import argparse
import csv
import json
import sqlite3
from pathlib import Path

from common import connect


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--project', required=True)
    p.add_argument('--format', choices=['json', 'csv'], default='json')
    args = p.parse_args()

    root = Path(args.project)
    con = connect(root)
    con.row_factory = sqlite3.Row
    tables = ['sources', 'evidence', 'competitors', 'customers', 'pricing', 'experiments', 'scores']
    data = {t: [dict(r) for r in con.execute(f'SELECT * FROM {t}')] for t in tables}
    con.close()

    out = root / 'exports'
    out.mkdir(exist_ok=True)
    if args.format == 'json':
        target = out / 'research-export.json'
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        print(target)
    else:
        for t, rows in data.items():
            if not rows:
                continue
            target = out / f'{t}.csv'
            with target.open('w', newline='', encoding='utf-8-sig') as f:
                w = csv.DictWriter(f, fieldnames=rows[0].keys())
                w.writeheader()
                w.writerows(rows)
        print(out)


if __name__ == '__main__':
    main()
