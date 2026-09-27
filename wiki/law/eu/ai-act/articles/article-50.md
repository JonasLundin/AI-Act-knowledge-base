---
type: Law
title: 'Article 50: Transparency Obligations for Certain AI Systems'
description: Mandates disclosure when humans interact with AI, watermarking of synthetic
  media, and deepfake disclosures.
category: law
tags:
- ai-act
- regulation
- article
- article-50
- transparency
- deepfakes
- watermarking
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
  provision: Article 50
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 50 (Transparency obligations for providers and deployers of certain AI systems)** establishes horizontal notification and transparency duties designed to protect citizens from deceptive or synthetic AI content[^regulation-eu-2024-1689].

# The Four Transparency Pillars

```
+-------------------------------------------------------------------+
|               ARTICLE 50 TRANSPARENCY MANDATE MATRIX              |
+-------------------------------------------------------------------+
| 1. AI-HUMAN INTERACTION (Article 50(1))                           |
|    - Providers must ensure AI systems interacting with natural    |
|      persons inform them that they are interacting with an AI     |
|      (e.g. conversational agents, automated chatbots).            |
+-------------------------------------------------------------------+
| 2. SYNTHETIC AUDIO, IMAGE, VIDEO, TEXT (Article 50(2))            |
|    - Providers of generative AI systems must mark outputs in a    |
|      machine-readable format and ensure they are detectable as    |
|      artificially generated (cryptographic watermarking/metadata).|
+-------------------------------------------------------------------+
| 3. EMOTION RECOGNITION & BIOMETRICS (Article 50(3))               |
|    - Deployers of emotion recognition or biometric categorization |
|      systems must inform individuals of their exposure.           |
+-------------------------------------------------------------------+
| 4. DEEP FAKES & PUBLIC INTEREST TEXT (Article 50(4))              |
|    - Deployers of deep fakes (manipulated image, audio, or video) |
|      must visibly and prominently disclose that content is        |
|      artificially created or manipulated.                         |
+-------------------------------------------------------------------+
```

# Machine-Readable Watermarking Standards
Under Article 50(2), watermarking techniques must be:
- State-of-the-art, robust, and tamper-resistant;
- Machine-detectable and readable across distribution platforms;
- Capable of surviving common compression, transcoding, and cropping transformations.

# Related concepts
- [Article 5: Prohibited AI Practices](article-5.md)
- [Article 52: GPAI Obligations](article-52.md)
- [Article 99: Administrative Fines](article-99.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
