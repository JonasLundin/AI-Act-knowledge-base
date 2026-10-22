---
type: Requirement
title: Synthetic Content Marking and Watermarking (Article 50(2))
description: Mandates providers of generative AI systems to mark synthetic audio,
  image, video, and text in machine-readable formats.
category: requirement
tags:
- ai-act
- obligations
- transparency
- article-50
- watermarking
- generative-ai
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
  provision: Article 50(2)
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 50(2)** of Regulation (EU) 2024/1689 imposes a legal duty on providers of AI systems generating synthetic audio, image, video, or text to ensure the outputs are marked in a machine-readable format and detectable as artificially generated or manipulated[^regulation-eu-2024-1689].

# Technical Requirements for Marking

```
+-------------------------------------------------------------------+
|               ARTICLE 50(2) WATERMARKING CRITERIA                 |
+-------------------------------------------------------------------+
| 1. TECHNICAL ROBUSTNESS                                           |
|    - Watermarks must be tamper-resistant, persistent across       |
|      compression, cropping, re-encoding, and file conversion.     |
+-------------------------------------------------------------------+
| 2. MACHINE-READABILITY                                            |
|    - Metadata and cryptographic signatures must follow open       |
|      standards (e.g. C2PA - Coalition for Content Provenance and  |
|      Authenticity).                                               |
+-------------------------------------------------------------------+
| 3. INTEROPERABILITY                                               |
|    - Marking techniques must be verifiable by online platforms,   |
|      search engines, and end-user verification tools.             |
+-------------------------------------------------------------------+
```

# Text Generation and Regulatory Derogations
- For AI text generation, marking is required unless the AI text has undergone a process of human review or editorial control and a natural or legal person holds editorial responsibility for the publication of the text.
- AI systems authorized by law for criminal detection/investigation are exempted.

# Related concepts
- [Transparency Obligations Index](index.md)
- [Deepfake Labelling](deepfake-labelling.md)
- [Article 50: Transparency Obligations](../../law/eu/ai-act/articles/article-50.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
