#!/usr/bin/env python3
"""Shared schema and connection helpers for the market-research scripts."""
import json
import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

SCHEMA = '''
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sources (
 id TEXT PRIMARY KEY, title TEXT NOT NULL, url TEXT NOT NULL UNIQUE,
 source_type TEXT, publisher TEXT, author TEXT, published_at TEXT,
 accessed_at TEXT, geography TEXT, relevance REAL DEFAULT 0.5,
 credibility REAL DEFAULT 0.5, notes TEXT, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS evidence (
 id TEXT PRIMARY KEY, claim TEXT NOT NULL, evidence_type TEXT NOT NULL,
 source_id TEXT, excerpt TEXT, interpretation TEXT, confidence REAL,
 counterevidence TEXT, status TEXT DEFAULT 'open', created_at TEXT NOT NULL,
 FOREIGN KEY(source_id) REFERENCES sources(id)
);
CREATE TABLE IF NOT EXISTS competitors (
 id TEXT PRIMARY KEY, name TEXT NOT NULL, url TEXT, category TEXT,
 target_customer TEXT, geography TEXT, business_model TEXT, pricing TEXT,
 strengths TEXT, weaknesses TEXT, positioning TEXT, distribution TEXT,
 user_signals TEXT, threat_level REAL DEFAULT 0.5, notes TEXT,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS customers (
 id TEXT PRIMARY KEY, segment TEXT NOT NULL, persona TEXT, role TEXT,
 problem TEXT, current_solution TEXT, pain_score REAL, urgency_score REAL,
 budget_score REAL, buying_trigger TEXT, blockers TEXT, source_id TEXT,
 notes TEXT, created_at TEXT NOT NULL,
 FOREIGN KEY(source_id) REFERENCES sources(id)
);
CREATE TABLE IF NOT EXISTS pricing (
 id TEXT PRIMARY KEY, segment TEXT NOT NULL, price REAL, currency TEXT,
 price_unit TEXT, arpu REAL, gross_margin REAL, implementation_cost REAL,
 support_cost REAL, sales_cycle_days INTEGER, conversion_rate REAL,
 cac REAL, payback_months REAL, retention_months REAL,
 break_even_customers INTEGER, notes TEXT, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS experiments (
 id TEXT PRIMARY KEY, name TEXT NOT NULL, hypothesis TEXT, target_segment TEXT,
 action TEXT, metric TEXT, threshold TEXT, deadline TEXT, kill_criteria TEXT,
 status TEXT DEFAULT 'planned', result TEXT, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS scores (
 id INTEGER PRIMARY KEY AUTOINCREMENT, dimension TEXT NOT NULL,
 score REAL NOT NULL, weight REAL NOT NULL, rationale TEXT, created_at TEXT NOT NULL
);
'''

REVERSE_SCORED = {'competition_intensity', 'risk'}


def connect(project):
    """Open the project SQLite database, ensuring the schema exists."""
    root = Path(project)
    db = root / 'market-research.db'
    con = sqlite3.connect(db)
    con.executescript(SCHEMA)
    return con


def load_jsonl_or_json(path):
    """Load records from either a JSON file (list) or a JSONL file."""
    text = Path(path).read_text(encoding='utf-8')
    if Path(path).suffix == '.json':
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]
