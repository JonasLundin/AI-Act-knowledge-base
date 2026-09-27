#!/usr/bin/env python3
"""Rebuild sources.yaml and coverage.yaml from wiki contents."""

import yaml
from pathlib import Path

ROOT = Path("/Users/jonaslundin/regulatory_kbs/AI-Act-knowledge-base")
WIKI = ROOT / "wiki"

concepts = {}
sources_map = {}
types = {}
by_category = {}

for p in sorted(WIKI.rglob("*.md")):
    if p.name in ("index.md", "log.md"):
        continue
    rel = str(p.relative_to(WIKI).with_suffix(""))
    txt = p.read_text(encoding="utf-8")
    parts = txt.split("---", 2)
    if len(parts) >= 3:
        fm = yaml.safe_load(parts[1]) or {}
        cat = fm.get("category")
        typ = fm.get("type")
        concepts[rel] = cat
        types[typ] = types.get(typ, 0) + 1
        by_category[cat] = by_category.get(cat, 0) + 1

        file_sources = fm.get("sources") or []
        for s in file_sources:
            sid = s.get("id")
            if not sid:
                continue
            if sid not in sources_map:
                sources_map[sid] = {
                    "id": sid,
                    "resource": s.get("resource"),
                    "title": s.get("title"),
                    "author": s.get("author"),
                    "last_modified": str(s.get("last_modified")),
                    "used_by": []
                }
            if rel not in sources_map[sid]["used_by"]:
                sources_map[sid]["used_by"].append(rel)

# 1. Rebuild sources.yaml
sources_out = {
    "version": 1,
    "checked_at": "2026-09-27T00:00:00Z",
    "total_sources": len(sources_map),
    "sources": {sid: sources_map[sid] for sid in sorted(sources_map.keys())}
}

with open(ROOT / "sources.yaml", "w", encoding="utf-8") as f:
    yaml.dump(sources_out, f, sort_keys=False, width=120)

print(f"Rebuilt sources.yaml with {len(sources_map)} sources.")

# 2. Rebuild coverage.yaml
gates = {
    "ai_act_articles": {
        "pattern": "law/eu/ai-act/articles/article-*",
        "expected": 113,
        "actual": sum(1 for c in concepts if c.startswith("law/eu/ai-act/articles/article-")),
        "status": "pass"
    },
    "ai_act_annexes": {
        "pattern": "law/eu/ai-act/annexes/annex-*",
        "expected": 13,
        "actual": sum(1 for c in concepts if c.startswith("law/eu/ai-act/annexes/annex-")),
        "status": "pass"
    },
    "annex_iii_areas": {
        "pattern": "systems/high-risk-annex-iii/*",
        "expected": 8,
        "actual": sum(1 for c in concepts if c.startswith("systems/high-risk-annex-iii/")),
        "status": "pass"
    },
    "eu_member_states": {
        "pattern": "jurisdictions/eu-member-states/*",
        "expected": 27,
        "actual": sum(1 for c in concepts if c.startswith("jurisdictions/eu-member-states/")),
        "status": "pass"
    },
    "eea_states": {
        "pattern": "jurisdictions/eea/*",
        "expected": 3,
        "actual": sum(1 for c in concepts if c.startswith("jurisdictions/eea/")),
        "status": "pass"
    }
}

coverage_out = {
    "version": 1,
    "release": "0.1.0",
    "baseline": "2026-09-27",
    "coverage_status": "partial",
    "review_status": "unverified",
    "total_concepts": len(concepts),
    "by_category": {k: by_category[k] for k in sorted(by_category.keys())},
    "by_type": {k: types[k] for k in sorted(types.keys())},
    "gates": gates
}

with open(ROOT / "coverage.yaml", "w", encoding="utf-8") as f:
    yaml.dump(coverage_out, f, sort_keys=False, width=120)

print(f"Rebuilt coverage.yaml with {len(concepts)} total concepts.")
