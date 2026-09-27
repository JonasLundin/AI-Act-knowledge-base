---
type: Law
title: 'Article 10: Data and Data Governance'
description: Mandates high-quality training, validation, and testing datasets, bias
  examination, and statistical data governance.
category: law
tags:
- ai-act
- regulation
- article
- article-10
- data-governance
- bias-mitigation
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
  provision: Article 10
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 10 (Data and data governance)** governs the data engineering, dataset curation, and quality management requirements for high-risk AI systems utilizing machine learning models[^regulation-eu-2024-1689].

Recognizing that algorithmic bias, discrimination, and hallucinations originate in flawed training datasets, Article 10 imposes strict quality and governance standards on data lifecycles.

# Mandatory Data Governance Practices (Article 10(2))

Training, validation, and testing datasets must be subject to appropriate data governance and management practices covering:

1. **Design Choices**: Explicit rationale for data selection, collection methods, and model feature representations.
2. **Data Provenance**: Documentation of data origin, collection protocols, original purpose of data collection, and labeling procedures.
3. **Data Preparation**: Cleaning, deduplication, imputation, aggregation, and normalization procedures.
4. **Formulation of Assumptions**: Explicit statement of assumptions regarding what the data is intended to measure or represent.
5. **Assessment of Data Availability & Gaps**: Identifying missing values, statistical anomalies, and demographic underrepresentation.
6. **Examination for Biases**: Systematic testing for biases that could lead to discrimination or disparate impact on protected groups (gender, race, age, disability).
7. **Appropriate Mitigation Measures**: Rebalancing, synthetic augmentation, or algorithmic debiasing to eliminate detected biases.

# Quality Criteria for Datasets (Article 10(3))
Datasets must be:
- **Relevant**: Statistically representative of the specific geographical, contextual, behavioral, or functional setting of intended use;
- **Sufficiently Free of Errors**: Cleaned and validated according to state-of-the-art data engineering practices;
- **Complete**: Possessing statistical properties necessary to generalize accurately across target user populations.

# Exception for Sensitive Data Processing (Article 10(5))
To the extent strictly necessary to detect and correct biases, providers may process special categories of personal data (GDPR Article 9(1) sensitive data) subject to stringent technical safeguards, pseudonymization, and state-of-the-art encryption.

# Related concepts
- [Article 9: Risk Management System](article-9.md)
- [Article 14: Human Oversight](article-14.md)
- [Fundamental Rights Impact Assessment (Article 27)](article-27.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
