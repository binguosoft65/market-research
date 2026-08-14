#!/usr/bin/env python3
import argparse, json, sqlite3, sys
from pathlib import Path
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    a=sub.add_parser('add'); a.add_argument('--project',required=True); a.add_argument('--file',required=True)
    l=sub.add_parser('list'); l.add_argument('--project',required=True)
    args=p.parse_args(); con=sqlite3.connect(Path(args.project)/'market-research.db')
    if args.cmd=='add':
        rows=json.loads(Path(args.file).read_text(encoding='utf-8')) if Path(args.file).suffix=='.json' else [json.loads(x) for x in Path(args.file).read_text(encoding='utf-8').splitlines() if x.strip()]
        for i,x in enumerate(rows,1):
            cid=x.get('id') or f'COMP-{i:04d}'
            con.execute('''INSERT INTO competitors(id,name,url,category,target_customer,geography,business_model,pricing,strengths,weaknesses,positioning,distribution,user_signals,threat_level,notes,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name,url=excluded.url,category=excluded.category,target_customer=excluded.target_customer,geography=excluded.geography,business_model=excluded.business_model,pricing=excluded.pricing,strengths=excluded.strengths,weaknesses=excluded.weaknesses,positioning=excluded.positioning,distribution=excluded.distribution,user_signals=excluded.user_signals,threat_level=excluded.threat_level,notes=excluded.notes''', (cid,x['name'],x.get('url'),x.get('category'),x.get('target_customer'),x.get('geography'),x.get('business_model'),x.get('pricing'),x.get('strengths'),x.get('weaknesses'),x.get('positioning'),x.get('distribution'),x.get('user_signals'),x.get('threat_level',0.5),x.get('notes'),datetime.now(timezone.utc).isoformat()))
        con.commit(); print(f'imported {len(rows)} competitors')
    else:
        for r in con.execute('SELECT id,name,category,target_customer,threat_level FROM competitors ORDER BY threat_level DESC'): print('\t'.join(map(str,r)))
    con.close()
if __name__=='__main__': main()
