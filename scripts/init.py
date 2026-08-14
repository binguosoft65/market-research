#!/usr/bin/env python3
import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from common import connect


def slugify(s):
    s = re.sub(r'[^\w\u4e00-\u9fff-]+', '-', s.strip().lower())
    s = re.sub(r'-+', '-', s).strip('-')
    return s or 'market-research'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('name')
    p.add_argument('--root', default='projects')
    p.add_argument('--mode', default='deep', choices=['quick', 'deep', 'validation'])
    p.add_argument('--geography', default='')
    p.add_argument('--segment', default='')
    p.add_argument('--budget', default='')
    p.add_argument('--advantages', default='')
    args = p.parse_args()

    slug = slugify(args.name)
    project = Path(args.root) / slug
    for d in ['sources', 'evidence', 'competitors', 'customers', 'pricing', 'experiments', 'reports', 'exports']:
        (project / d).mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()
    con = connect(project)
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('project_name', args.name))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('slug', slug))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('mode', args.mode))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('geography', args.geography))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('target_segment', args.segment))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('budget', args.budget))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('founder_advantages', args.advantages))
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", ('created_at', now))
    con.commit()
    con.close()

    cfg = {
        'name': args.name,
        'slug': slug,
        'mode': args.mode,
        'geography': args.geography,
        'target_segment': args.segment,
        'budget': args.budget,
        'founder_advantages': args.advantages,
        'decision': 'Should we pursue this market/opportunity?',
        'created_at': now,
        'weights': {
            'market_attractiveness': 0.12,
            'growth': 0.08,
            'customer_pain': 0.15,
            'willingness_to_pay': 0.12,
            'competition_intensity': 0.10,
            'acquisition_feasibility': 0.12,
            'delivery_feasibility': 0.10,
            'one_person_fit': 0.10,
            'defensibility': 0.06,
            'risk': 0.05,
        },
    }
    (project / 'research.yaml').write_text(
        yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding='utf-8'
    )
    print(f'PROJECT={project}')
    print(f'DB={project / "market-research.db"}')


if __name__ == '__main__':
    main()
