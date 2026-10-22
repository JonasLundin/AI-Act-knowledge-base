# AI Act Knowledge Base

An English-language [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle covering the EU Artificial Intelligence Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744), its delegated and implementing acts, the standardisation work behind it, the AI Office and national authorities, and the official guidance.

The bundle will contain concise original summaries with provision-level citations to primary sources. It does not reproduce full legal instruments, rules, guidance documents, or standards.

Current release: **0.1.0** (see [CHANGELOG.md](CHANGELOG.md))

> **General orientation only:** once populated, do not rely on this knowledge base for decisions that determine, demonstrate, or materially affect legal or regulatory compliance. Verify the current primary sources and obtain qualified professional advice before making AI-system classification, prohibited-practice, conformity-assessment, market-access, transparency, incident-reporting, or other compliance-impacting decisions.

## Use With Meerkat

[Meerkat](https://github.com/zegit-zoo/meerkat) can serve the bundle as CLI, MCP, or HTTP without conversion:

```sh
mk --kb-dir . search "high-risk classification"
mk --kb-dir . show law/eu/ai-act/articles/article-6
mk --kb-dir . list --category law
mk --kb-dir . mcp serve
mk --kb-dir . http serve --port 4004
```

Run these commands from the repository root. The knowledge bundle itself is under `wiki/`; Meerkat's `--kb-dir` reads that content-repository layout. The paths above are the planned concept IDs and resolve once ingestion has reached them.

The Markdown remains usable without Meerkat or any other tool.

## Coverage

The intended corpus includes:

- Regulation (EU) 2024/1689, its 13 annexes, Regulation (EU) 2026/1744 and later secondary legislation;
- obligations by role: providers, deployers, importers, distributors, authorised representatives, GPAI providers;
- risk categories and Annex III areas;
- the standardisation request, JTC 21 work and OJEU citations;
- AI Office, Commission and EDPB guidance;
- national authorities, sandboxes and penalties for the 27 Member States and EEA status;
- interacting EU legislation, in particular CRA Article 12.

Coverage is measured in `coverage.yaml`. Each gate names a glob over `wiki/`, the expected number of concepts where the corpus is finite, and the count actually present. A missing official source is recorded as a research gap rather than filled by inference.

## Structure

`kb.yaml` declares the bundle's slug, extension key (`x-ai-act`), categories and sections. Every section has an `index.md` describing what belongs there.

| Section | Contents |
|---|---|
| [`law/`](wiki/law/index.md) | Regulation (EU) 2024/1689 article by article, its annexes, the amending Regulation (EU) 2026/1744, delegated and implementing acts, and interacting EU law. |
| [`obligations/`](wiki/obligations/index.md) | Role and lifecycle views of the regulation's requirements. |
| [`systems/`](wiki/systems/index.md) | The regulation's risk categories and the systems that fall into each. |
| [`standards/`](wiki/standards/index.md) | Harmonised standards, the standardisation request to CEN and CENELEC, JTC 21 work items, common specifications, and supporting international standards recorded as identifiers and links. |
| [`guidance/`](wiki/guidance/index.md) | Official non-binding guidance. |
| [`authorities/`](wiki/authorities/index.md) | EU-level governance: the AI Office, the European Artificial Intelligence Board, the Scientific Panel, the Advisory Forum, notified bodies as a role, and the market surveillance framework. |
| [`jurisdictions/`](wiki/jurisdictions/index.md) | Each Member State's market surveillance and notifying authorities, regulatory sandboxes, penalties and implementing measures, plus EEA status. |
| [`timeline/`](wiki/timeline/index.md) | Entry into force, prohibited practices, GPAI obligations, Article 50 transparency, the deferred high-risk dates under Regulation (EU) 2026/1744, standardisation and review milestones. |
| [`glossary/`](wiki/glossary/index.md) | Terms defined in Article 3 of Regulation (EU) 2024/1689. |

## Source And Publication Policy

- Binding claims cite OJEU, ELI, EUR-Lex, or an official national gazette.
- Official guidance is labelled non-binding.
- A standard provides presumption of conformity only when its reference is cited in the OJEU for the requirements concerned.
- Publicly accessible drafts are linked, not copied.
- Articles are summarised in their consolidated form; each amendment is recorded on the amendments pages with the date it took effect.
- Dates changed by Regulation (EU) 2026/1744 are stated with both the original and the amended date.
- Agent-generated content stays `status: draft` until a human verifies it against the cited source.
- Superseded material is retained and marked rather than silently deleted.

This repository is not legal advice, is not a conformity assessment, does not certify any product or organisation, and must not be used as the basis for compliance-impacting decisions.

## Validate

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest tools/test_validate.py
python3 tools/validate.py wiki
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections with exact primary-source citations are welcome. Do not submit copied standards text, private compliance evidence, or confidential information.

## Related Knowledge Bases

- [CRA-knowledge-base](https://github.com/JonasLundin/CRA-knowledge-base): Regulation (EU) 2024/2847, the Cyber Resilience Act
- [NIS2-knowledge-base](https://github.com/JonasLundin/NIS2-knowledge-base): Directive (EU) 2022/2555 and its national transpositions
- [CVD-knowledge-base](https://github.com/JonasLundin/CVD-knowledge-base): coordinated vulnerability disclosure, the CVE Program, CSAF, VEX and scoring
- [Conformity-Assessment-knowledge-base](https://github.com/JonasLundin/Conformity-Assessment-knowledge-base): the New Legislative Framework, modules, accreditation and notified bodies
- [Software-Supply-Chain-knowledge-base](https://github.com/JonasLundin/Software-Supply-Chain-knowledge-base): SBOM formats, attestation, provenance and VEX
- [NIST-CSF-knowledge-base](https://github.com/JonasLundin/NIST-CSF-knowledge-base): NIST Cybersecurity Framework 2.0
- [knowledge-base-template](https://github.com/JonasLundin/knowledge-base-template): the shared template every bundle in the series is built from

## Licence

Original summaries, structure, and metadata are licensed under [CC BY 4.0](LICENSE). Source documents, rules, specifications and standards retain their own terms; see [NOTICE](NOTICE).

This project is independent and is not affiliated with or endorsed by the European Commission, the AI Office, the European Artificial Intelligence Board, the EDPB, any national authority, CEN, CENELEC, ETSI, ISO, IEC, Google Cloud, or Meerkat. Repository: https://github.com/JonasLundin/AI-Act-knowledge-base
