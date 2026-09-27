---
type: Concept
title: Systemic Risk GPAI Obligations (Article 55)
description: Mandates providers of GPAI models with systemic risk (>10^25 FLOPs) to
  perform model evaluations, adversarial testing, track serious incidents, and ensure
  cybersecurity.
category: requirement
tags:
- ai-act
- obligations
- gpai
- systemic-risk
- article-55
- red-teaming
status: draft
generated:
  by: agent:kb-researcher-writer
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
  provision: Article 55
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 55** of Regulation (EU) 2024/1689 sets out enhanced risk management duties for providers of **GPAI models with systemic risk** (models designated under Article 51 or having cumulative training compute exceeding $10^{25}$ FLOPs)[^regulation-eu-2024-1689].

# Mandatory Systemic Risk Controls
1. **Model Evaluation & Red-Teaming (Point a)**: Conduct rigorous model evaluations, including standardized red-teaming and adversarial testing, to identify systemic vulnerabilities and risks of CBRN or cyberattack amplification.
2. **Mitigation of Systemic Risks (Point b)**: Assess and mitigate potential systemic risks at Union level.
3. **Serious Incident Tracking & Reporting (Point c)**: Document and immediately report serious incidents and corrective measures to the European AI Office and national CSIRTs.
4. **Cybersecurity Safeguards (Point d)**: Ensure state-of-the-art physical and cyber protection for model weights, training infrastructure, and execution clusters.

# Related concepts
- [GPAI Obligations Index](index.md)
- [GPAI Baseline Obligations](gpai-baseline-obligations.md)
- [Article 51: Systemic Risk Criteria](../../law/eu/ai-act/articles/article-51.md)
- [Article 55: Systemic Risk Obligations](../../law/eu/ai-act/articles/article-55.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
