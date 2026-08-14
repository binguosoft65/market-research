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
    p=argparse.ArgumentParser(); p.add_argument('--project',required=True); p.add_argument('--file',required=True)
    a=p.parse_args(); root=Path(a.project); db=root/'market-research.db'; now=datetime.now(timezone.utc).isoformat()
    con=sqlite3.connect(db); count=0
    for line in Path(a.file).read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        x=json.loads(line); sid=x.get('id') or f"SRC-{count+1:04d}"
        con.execute('''INSERT INTO sources(id,title,url,source_type,publisher,author,published_at,accessed_at,geography,relevance,credibility,notes,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET title=excluded.title,url=excluded.url,source_type=excluded.source_type,publisher=excluded.publisher,author=excluded.author,published_at=excluded.published_at,accessed_at=excluded.accessed_at,geography=excluded.geography,relevance=excluded.relevance,credibility=excluded.credibility,notes=excluded.notes''', (sid,x['title'],x['url'],x.get('source_type'),x.get('publisher'),x.get('author'),x.get('published_at'),x.get('accessed_at'),x.get('geography'),x.get('relevance',0.5),x.get('credibility',0.5),x.get('notes'),now)); count+=1
    con.commit(); con.close(); print(f'ingested {count} sources')
if __name__=='__main__': main()
