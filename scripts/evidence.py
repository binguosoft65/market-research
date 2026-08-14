#!/usr/bin/env python3
import argparse, sqlite3, sys
from pathlib import Path
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    a=sub.add_parser('add'); a.add_argument('--project',required=True); a.add_argument('--claim',required=True); a.add_argument('--type',required=True,choices=['FACT','INFERENCE','HYPOTHESIS','UNKNOWN']); a.add_argument('--source'); a.add_argument('--text',default=''); a.add_argument('--interpretation',default=''); a.add_argument('--confidence',type=float,default=0.5); a.add_argument('--counterevidence',default='')
    l=sub.add_parser('list'); l.add_argument('--project',required=True)
    args=p.parse_args(); con=sqlite3.connect(Path(args.project)/'market-research.db');
    if args.cmd=='add':
        cur=con.execute('SELECT COALESCE(MAX(CAST(SUBSTR(id,5) AS INTEGER)),0)+1 FROM evidence WHERE id LIKE "EVD-%"'); n=cur.fetchone()[0]; eid=f'EVD-{n:04d}'
        con.execute('INSERT INTO evidence(id,claim,evidence_type,source_id,excerpt,interpretation,confidence,counterevidence,created_at) VALUES(?,?,?,?,?,?,?,?,?)',(eid,args.claim,args.type,args.source,args.text,args.interpretation,args.confidence,args.counterevidence,datetime.now(timezone.utc).isoformat())); con.commit(); print(eid)
    else:
        for r in con.execute('SELECT id,evidence_type,claim,source_id,confidence FROM evidence ORDER BY id'): print('\t'.join(map(str,r)))
    con.close()
if __name__=='__main__': main()
