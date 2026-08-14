#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
from pathlib import Path

import yaml

from common import REVERSE_SCORED, connect

DIMENSIONS = [
    'market_attractiveness', 'growth', 'customer_pain', 'willingness_to_pay',
    'competition_intensity', 'acquisition_feasibility', 'delivery_feasibility',
    'one_person_fit', 'defensibility', 'risk',
]


def main():
    p = argparse.ArgumentParser(
        description='Compute a weighted opportunity score. '
                    'competition_intensity and risk are reverse-scored: '
                    'enter 10 for the worst case, and the script inverts them.'
    )
    p.add_argument('--project', required=True)
    p.add_argument('--scores', nargs='*', help='dimension=value pairs (0-10)')
    args = p.parse_args()

    root = Path(args.project)
    cfg = yaml.safe_load((root / 'research.yaml').read_text(encoding='utf-8'))
    weights = cfg['weights']

    supplied = {}
    for item in args.scores or []:
        k, v = item.split('=', 1)
        supplied[k] = float(v)

    defaults = {dim: 5 for dim in DIMENSIONS}
    vals = {**defaults, **supplied}

    con = connect(root)
    con.execute('DELETE FROM scores')
    now = datetime.now(timezone.utc).isoformat()
    total = 0.0
    for dim, w in weights.items():
        s = max(0, min(10, float(vals.get(dim, 5))))
        effective = (10 - s) if dim in REVERSE_SCORED else s
        total += effective * w
        rationale = (
            f'Reverse-scored (raw {s}, effective {effective})' if dim in REVERSE_SCORED
            else 'Agent-entered score; rationale should be documented in the report.'
        )
        con.execute(
            'INSERT INTO scores(dimension, score, weight, rationale, created_at) '
            'VALUES(?,?,?,?,?)',
            (dim, s, w, rationale, now),
        )
    con.commit()
    con.close()
    print(f'{total:.2f}/10')


if __name__ == '__main__':
    main()
