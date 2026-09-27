---
type: Concept
title: Data and Data Governance Obligations (Article 10 & 16(b))
description: Statutory requirements for training, validation, and testing datasets,
  bias examination, and statistical curation.
category: requirement
tags:
- ai-act
- obligations
- providers
- high-risk
- article-10
- data-governance
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
  provision: Article 10, Article 16(b)
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

Under **Article 16(b)** and **Article 10** of Regulation (EU) 2024/1689, providers must develop high-risk AI systems based on training, validation, and testing datasets that meet strict quality and data governance criteria[^regulation-eu-2024-1689].

# Data Governance Dimensions
- **Provenance & Design Choices**: Detailed documentation of data collection and labeling protocols.
- **Bias Detection**: Pre-deployment examination to identify demographic or geographic biases.
- **Dataset Representativeness**: Ensuring datasets have statistically valid representation for the target deployment context.
- **Sensitive Data Exception (Article 10(5))**: Explicit permission to process GDPR Article 9 special categories of data strictly for bias mitigation under technical safeguards.

# Related concepts
- [Provider Obligations Index](index.md)
- [Risk Management Obligations](risk-management-obligations.md)
- [Article 10: Data and Data Governance](../../law/eu/ai-act/articles/article-10.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
