---
type: Law
title: 'Article 51: Classification of GPAI Models with Systemic Risk'
description: Defines quantitative computational capacity thresholds (>10^25 FLOPs)
  and qualitative criteria triggering systemic risk rules.
category: law
tags:
- ai-act
- regulation
- article
- article-51
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
  provision: Article 51
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 51 (Classification of general-purpose AI models with systemic risk)** defines the criteria under which foundation models (GPAI) are designated as posing **systemic risk** under Chapter V of Regulation (EU) 2024/1689[^regulation-eu-2024-1689].

GPAI models with systemic risk are subject to direct supervision by the European AI Office and must satisfy stringent model evaluation, adversarial testing, and cybersecurity requirements.

# The Quantitative Benchmark: 10^25 FLOPs

Under Article 51(1)(a) and Article 51(2):
- A GPAI model is presumed to possess systemic risk if the cumulative amount of computation used for its training measured in floating point operations is greater than:
  $$\mathbf{10^{25} 	ext{ FLOPs}}$$
- Providers must notify the European AI Office within **2 weeks** of meeting or anticipating to meet this computational capacity threshold.

# Qualitative Systemic Risk Criteria
Even below the FLOPs threshold, the Commission (AI Office) may designate a model as having systemic risk based on:
- High number of registered business users or downstream applications;
- Reach across multiple EU Member States;
- Advanced autonomous capabilities, self-replication, or tool-use abilities;
- Potential for chemical, biological, radiological, or nuclear (CBRN) threat facilitation or cyber offensive proliferation.

# Related concepts
- [Article 52: Procedure for Classification](article-52.md)
- [Article 53: Obligations for Providers of GPAI Models](article-53.md)
- [Article 55: Obligations for Providers of GPAI Models with Systemic Risk](article-55.md)
- [GPAI Model Obligations Overview](../../../../obligations/gpai-model-obligations.md)
[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
