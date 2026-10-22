---
type: Requirement
title: AI-Human Interaction Disclosure (Article 50(1))
description: Mandatory obligation for providers to ensure AI systems interacting with
  natural persons inform them that they are interacting with AI.
category: requirement
tags:
- ai-act
- obligations
- transparency
- article-50
- chatbots
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
  provision: Article 50(1)
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 50(1)** of Regulation (EU) 2024/1689 mandates that providers of AI systems intended to interact directly with natural persons must design and develop them in such a way that the affected persons are informed that they are interacting with an AI system[^regulation-eu-2024-1689].

# Statutory Requirements

1. **Timely Disclosure**: The notification must be provided at the very beginning of the interaction, prior to any exchange of substantive information.
2. **Clarity and Prominence**: The notice must be clear, salient, and intelligible to the average user, taking into account the context and characteristics of natural persons (e.g. vulnerable users, children).
3. **Exceptions**:
   - Circumstances where it is obvious from the point of view of a reasonable natural person from the context of use (e.g., interacting with a robotic hardware device clearly marked as a robot).
   - AI systems authorized by law to detect, prevent, investigate, or prosecute criminal offences, subject to appropriate procedural safeguards.

# Implementation Architecture

```
+-------------------------------------------------------------+
|                AI INTERACTION DISCLOSURE FLOW               |
+-------------------------------------------------------------+
| [User Session Start]                                        |
|         |                                                   |
|         v                                                   |
| [Display Explicit AI Notice: "You are speaking with an AI"] |
|         |                                                   |
|         v                                                   |
| [User Interaction & Conversation]                           |
+-------------------------------------------------------------+
```

# Related concepts
- [Transparency Obligations Index](index.md)
- [Synthetic Content Marking & Watermarking](synthetic-content-marking.md)
- [Deepfake Labelling](deepfake-labelling.md)
- [Article 50: Transparency Obligations](../../law/eu/ai-act/articles/article-50.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
