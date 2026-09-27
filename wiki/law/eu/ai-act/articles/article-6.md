---
type: Law
title: 'Article 6: Classification Rules for High-Risk AI Systems'
description: Defines the two-tier classification mechanism designating AI systems
  as high-risk under Annex I and Annex III.
category: law
tags:
- ai-act
- regulation
- article
- article-6
status: draft
generated:
  by: agent:antigravity
  at: '2026-09-27T00:00:00Z'
stale_after: '2027-12-31T00:00:00Z'
sources:
- id: regulation-eu-2024-1689
  resource: http://data.europa.eu/eli/reg/2024/1689/oj
  title: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence
    (Artificial Intelligence Act)
  author: European Parliament and Council of the European Union
  last_modified: '2024-07-12T00:00:00Z'
x-ai-act:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 6
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 6 (Classification rules for high-risk AI systems)** establishes the legal gateway determining whether an AI system falls into the strictly regulated **High-Risk** category under Regulation (EU) 2024/1689[^regulation-eu-2024-1689].

High-risk classification triggers mandatory compliance with Chapter III requirements (risk management, data governance, technical documentation, human oversight, cybersecurity) and conformity assessment prior to deployment.

# The Two Classification Pathways

```
                          AI SYSTEM CLASSIFICATION
                                     |
               +---------------------+---------------------+
               |                                           |
               v                                           v
      ARTICLE 6(1): ANNEX I                       ARTICLE 6(2): ANNEX III
   (Safety Component in Harmonised             (Stand-Alone High-Risk Use Cases)
          EU Products)                                     |
               |                               8 Critical Domains:
   - Medical Devices (MDR/IVDR)                - Biometrics & Identification
   - Machinery Regulation                      - Critical Infrastructure
   - Civil Aviation & Vehicles                 - Education & Vocational Training
   - Radio Equipment                           - Employment & Worker Management
   - Toys, Lifts, Marine Eq.                   - Essential Public/Private Services
                                               - Law Enforcement
                                               - Migration, Asylum & Border Control
                                               - Administration of Justice
```

# The Article 6(3) Derogation (The Risk Filter)
An AI system listed in Annex III is **not** considered high-risk if it does not pose a significant risk of harm to health, safety, or fundamental rights, satisfying one of four conditions:
1. Performs a narrow procedural task;
2. Improves the result of a previously completed human activity;
3. Detects decision-making patterns without replacing human assessment; or
4. Performs only preparatory tasks for assessment.

*Note*: An AI system that always performs profiling of natural persons is ALWAYS considered high-risk, without exemption.

# Related concepts
- [Article 5: Prohibited AI Practices](article-5.md)
- [Article 9: Risk Management System](article-9.md)
- [Article 16: Obligations of Providers of High-Risk AI Systems](article-16.md)
[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
