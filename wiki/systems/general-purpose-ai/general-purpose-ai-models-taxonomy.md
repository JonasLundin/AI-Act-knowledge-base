---
type: Concept
title: General-Purpose AI Models Taxonomy
description: Classification of GPAI models into baseline models versus models with
  systemic risk exceeding 10^25 FLOPs.
category: system
tags:
- ai-act
- systems
- gpai
- systemic-risk
- article-51
- flops
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
  provision: Article 51, Article 52
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

Regulation (EU) 2024/1689 establishes a dedicated regulatory framework for **General-Purpose AI (GPAI) Models** based on a tiered capability architecture[^regulation-eu-2024-1689].

# The Dual-Tier GPAI Classification
1. **Tier 1: Standard GPAI Models**:
   - Models displaying significant generality capable of performing a wide range of distinct tasks.
   - Subject to baseline transparency, technical documentation, copyright policy, and training data summaries (Article 53).
2. **Tier 2: GPAI Models with Systemic Risk**:
   - Models possessing high-impact capabilities evaluated by appropriate benchmarks, or
   - Models trained with cumulative computational capacity exceeding **$10^{25}$ integer or floating-point operations (FLOPs)**.
   - Subject to red-teaming, adversarial evaluation, severe incident tracking, and cybersecurity controls (Article 55).

# Related concepts
- [General-Purpose AI Index](index.md)
- [Article 51: Systemic Risk Criteria](../../law/eu/ai-act/articles/article-51.md)
- [GPAI Baseline Obligations](../../obligations/general-purpose-ai/gpai-baseline-obligations.md)
- [Systemic Risk GPAI Obligations](../../obligations/general-purpose-ai/gpai-systemic-risk-obligations.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
