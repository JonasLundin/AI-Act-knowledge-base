---
type: Law
title: 'Article 14: Human Oversight'
description: Mandates human-in-the-loop and human-on-the-loop mechanisms, stop-buttons,
  and mitigation of automation bias.
category: law
tags:
- ai-act
- regulation
- article
- article-14
- human-oversight
- automation-bias
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
  provision: Article 14
  checked_at: '2026-09-27T00:00:00Z'
---

# Summary

**Article 14 (Human oversight)** mandates that high-risk AI systems must be designed and developed with operational interfaces that enable natural persons to oversee their functioning during deployment[^regulation-eu-2024-1689].

The objective of Article 14 is to prevent or minimize risks to health, safety, and fundamental rights by preventing automated decisions from escaping effective human control.

# The Three Human Oversight Operating Models

```
+-------------------------------------------------------------------+
|               ARTICLE 14 HUMAN OVERSIGHT ARCHITECTURES            |
+-------------------------------------------------------------------+
| 1. HUMAN-IN-THE-LOOP (HITL)                                       |
|    - Human must actively review, validate, and sign off on every  |
|      single output/decision before it takes legal or physical     |
|      effect.                                                      |
+-------------------------------------------------------------------+
| 2. HUMAN-ON-THE-LOOP (HOTL)                                       |
|    - System operates autonomously under real-time human monitoring|
|      with capability for immediate human intervention or override |
|      at any step.                                                 |
+-------------------------------------------------------------------+
| 3. HUMAN-IN-COMMAND (HIC)                                         |
|    - Human retains supreme operational authority, overseeing the  |
|      entire system activity with ability to shut down, disengage, |
|      or stop the system via a fail-safe 'kill-switch'.            |
+-------------------------------------------------------------------+
```

# Mandatory Capabilities of Overseeing Individuals (Article 14(4))
The technical interface must enable human overseers to:
1. **Understand Capabilities & Limitations**: Fully understand the system's operational constraints and monitor its activity;
2. **Combat Automation Bias**: Remain aware of the tendency to automatically rely on or over-trust AI recommendations ("automation bias");
3. **Interpret Outputs**: Correctly interpret system predictions, confidence scores, and reasoning;
4. **Override or Reverse**: Decide not to use the AI system, ignore its recommendations, or manually override its decisions;
5. **Interrupt & Stop**: Intervene at any moment to halt execution via a secure stop button or emergency procedure.

# Related concepts
- [Article 9: Risk Management System](article-9.md)
- [Article 26: Deployer Obligations](article-26.md)
- [Fundamental Rights Impact Assessment (Article 27)](article-27.md)

[^regulation-eu-2024-1689]: European Parliament and Council of the European Union, Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), http://data.europa.eu/eli/reg/2024/1689/oj
