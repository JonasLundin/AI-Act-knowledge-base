---
type: Law
title: 'Article 6: Classification Rules for High-Risk AI Systems'
description: Defines the two classification gateways for high-risk AI systems (Annex I product safety components and Annex III standalone systems) and Article 6(3) derogation rules.
category: law
tags:
- ai-act
- regulation
- article
- article-6
- classification
- high-risk
status: draft
generated:
  by: agent:kb-researcher-writer
  at: '2026-09-27T00:00:00Z'
stale_after: '2027-12-02T00:00:00Z'
sources:
- id: regulation-eu-2024-1689
  resource: http://data.europa.eu/eli/reg/2024/1689/oj
  title: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)
  author: European Parliament and Council of the European Union
  last_modified: '2024-07-12T00:00:00Z'
- id: regulation-eu-2026-1744
  resource: http://data.europa.eu/eli/reg/2026/1744/oj
  title: Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)
  author: European Parliament and Council of the European Union
  last_modified: '2026-07-08T00:00:00Z'
x-ai-act:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 6
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 6 (Classification rules for high-risk AI systems)** establishes the legal architecture determining whether an AI system is subject to the mandatory Chapter III obligations[^regulation-eu-2024-1689].

# The Dual High-Risk Classification Architecture

```
+-------------------------------------------------------------------+
|               ARTICLE 6 HIGH-RISK GATEWAY MATRIX                  |
+-------------------------------------------------------------------+
| GATEWAY 1: EMBEDDED SAFETY COMPONENTS (Article 6(1))              |
| The AI system is a safety component of, or is itself, a product    |
| covered by Union harmonisation legislation listed in Annex I AND   |
| requires third-party conformity assessment under that legislation.|
| -> Application date: 2 August 2028 (amended by Reg (EU) 2026/1744).|
+-------------------------------------------------------------------+
| GATEWAY 2: STANDALONE HIGH-RISK AREAS (Article 6(2))               |
| The AI system falls within one of the eight critical societal      |
| domains explicitly enumerated in Annex III (biometrics, critical   |
| infrastructure, education, employment, public services, etc.).     |
| -> Application date: 2 December 2027 (amended by Reg (EU) 2026/1744)|
+-------------------------------------------------------------------+
```

# Safety Component Clarifications (Article 6(1a)–(1c))
Inserted by Regulation (EU) 2026/1744[^regulation-eu-2026-1744]:
- **Paragraph 1a**: Clarifies that AI systems used for purposes other than the safety functions of products covered by Annex I Union harmonisation legislation are excluded from the scope of high-risk classification under paragraph 1 (non-safety uses excluded).
- **Paragraph 1b**: Clarifies that an AI system that is a safety component of a product, or is itself a product, which endangers the health or safety of persons is included as high-risk even if not specifically identified under Annex I (health/safety-endangering AI included).
- **Paragraph 1c**: Specifies that where third-party conformity assessment under Annex I Union harmonisation legislation addresses aspects other than health and safety (e.g. electromagnetic compatibility or energy labelling alone), such assessment does not satisfy the condition of Article 6(1)(b) (non-H&S third-party assessment does not meet 6(1)(b)).

# The Article 6(3) Derogation
An AI system listed in Annex III is **not** high-risk if it does not pose a significant risk of harm to health, safety, or fundamental rights, satisfying one of four conditions:
1. Performs a narrow procedural task;
2. Improves the result of a previously completed human activity;
3. Detects decision-making patterns without replacing previous human assessments;
4. Performs preparatory tasks for assessment in Annex III use cases.

*Exception*: If the system performs profiling of natural persons, it is **always** high-risk.

# Related concepts
- [Article 5: Prohibited AI Practices](article-5.md)
- [Article 7: Amendments to Annex III](article-7.md)
- [Article 16: Obligations of Providers of High-Risk AI Systems](article-16.md)
- [Article 113: Entry into Force and Application](article-113.md)
- [Annex III High-Risk AI Systems](../annexes/annex-3.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
[^regulation-eu-2026-1744]: European Parliament and Council of the European Union, Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI), http://data.europa.eu/eli/reg/2026/1744/oj
