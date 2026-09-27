---
type: Requirement
title: General-Purpose AI (GPAI) Model Obligations
description: Comprehensive operational breakdown of provider obligations for standard
  GPAI models and models with systemic risk.
category: requirement
tags:
- ai-act
- obligation
- gpai-model-obligations
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
  provision: Articles 53, 55
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

Chapter V of Regulation (EU) 2024/1689 establishes a tiered governance regime for providers of **General-Purpose AI (GPAI) models** (foundation models, LLMs, multimodal systems)[^regulation-eu-2024-1689].

# Tier 1: Baseline GPAI Obligations (Article 53)
All providers placing a GPAI model on the Union market must:
1. **Technical Documentation**: Draw up and maintain technical documentation detailing training and testing processes, evaluation results, and model architecture.
2. **Downstream Transparency**: Provide information and documentation to downstream AI system providers intending to integrate the model into high-risk AI systems.
3. **Copyright Compliance**: Put in place a policy to comply with Union copyright law (Directive (EU) 2019/790), respecting machine-readable rights reservations.
4. **Training Data Summary**: Make publicly available a sufficiently detailed summary of the content used for training the GPAI model, following a template provided by the AI Office.

# Tier 2: GPAI with Systemic Risk Obligations (Article 55)
In addition to baseline obligations, providers of models meeting the $>10^{25}$ FLOPs threshold must:
1. **Model Evaluations**: Perform state-of-the-art model evaluations, including standardized red-teaming and adversarial testing.
2. **Systemic Risk Mitigation**: Assess and mitigate systemic risks at Union level (e.g. CBRN proliferation, mass cyberattacks, algorithmic bias).
3. **Serious Incident Tracking**: Track, document, and report serious incidents and corrective measures to the AI Office and national authorities without undue delay.
4. **Adequate Cybersecurity**: Implement state-of-the-art cybersecurity protections for the model weights, training infrastructure, and distribution endpoints.

# Related concepts
- [Article 51: Classification of GPAI Models with Systemic Risk](../law/eu/ai-act/articles/article-51.md)
- [Article 53: Obligations for Providers of GPAI Models](../law/eu/ai-act/articles/article-53.md)
- [Provider Obligations Overview](provider-obligations.md)
[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
