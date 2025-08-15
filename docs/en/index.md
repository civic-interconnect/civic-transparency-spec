# Civic Transparency (Draft)

> **Provenance & Behavior Transparency**  
> An exploratory, privacy-respecting framework for understanding how public content spreads online.

- [GitHub Repository](https://github.com/civic-interconnect/civic-transparency-spec)
- [Hosted Draft Documentation](https://civic-interconnect.github.io/civic-transparency-spec/)

This site documents **experimental schema drafts** and research ideas under active development.

---

## Project Vision

Explore the feasibility of a behavioral transparency dashboard that:

- Ingests public, ToS-compliant data from platforms with usable APIs.
- Surfaces burst activity, coordination, and automation patterns without analyzing post content.
- Publishes **aggregated behavioral signals** rather than identifying individuals.
- Offers exploration tools for researchers, journalists, and civic technologists.

---

## Motivation

Online manipulation thrives in opacity.  
We do **not** judge message content or viewpoints.  
Instead, we visualize **how** content spreads.

For platforms, our goal is to use **low-cost metadata** and aggregation methods to minimize operational risk and simplify adoption.

---

## Exploratory Model

1. **Provenance Tags**  
   A proposed schema of non-identifying metadata at post time:
   - Account age bucket  
   - Reshare flag  
   - Media reuse flag  
   - Automation status (if detectable)

2. **Transparency Endpoint**  
   A low-cost, unauthenticated API that platforms could expose:
   - Input: trend, hashtag, or topic  
   - Output: anonymized stats by signal type and time range

3. **Privacy by Design**
   - No identifiers or message content
   - Only aggregated results  
   - Bucketed metrics (e.g., k ≥ 100)  
   - No user scoring or permanent identifiers

---

## Why Might Platforms Participate?

- **Proactive trust-building.**  
  Offers visibility without revealing users.

- **Low overhead.**  
  Metadata is computed once; aggregation is lightweight.

- **Regulatory alignment.**  
  Potential fit with EU DSA and similar transparency mandates.

---

## Why It Might Help the Public

- **Fact-checkers and journalists** can analyze trend origin and scale.  
- **Civic groups** can detect astroturfing or amplification.  
- **Voters and researchers** gain clarity on coordination dynamics.

---

## Design Principles

- **Behavioral, not ideological.**  
  No classification of content or users.

- **No centralized authority.**  
  All methods and signals are open for review and critique.

- **Aggregate-first.**  
  Computation happens internally; only grouped results are published.

---

## Areas of Exploration

- Account age skews
- Reshared/recycled media bursts
- Hashtag/topic-level automation rates
- Coordinated posting patterns
- Platform-agnostic schema and API prototypes

---

## Privacy and Safety

**What this project does NOT do:**

- Reveal individual users, IP addresses, or message content  
- Classify sentiment, misinformation, or intent  
- Score users or create reputational data  
- Interfere with private communications

---

## Risks We Consider

- **Evasion tactics**: actors may adapt  
  → Combine multiple signals, refine methods

- **Gaming behavior**: flooding or noise  
  → Multi-modal analysis (e.g., media hashes, URL reuse)

- **Public discomfort**: perceived surveillance  
  → Keep all outputs non-personal and non-identifying

---

## Exploratory Outcomes (Hypothetical)

- **Short term**: Coordination visualizations inform journalists  
- **Mid term**: Platforms experiment with test implementations  
- **Long term**: Shared civic infrastructure to spot manipulation early

---

## More (Draft) Docs

- [Glossary](./docs/glossary.md)
- [Metrics](./docs/metrics.md)
- [Privacy](./docs/privacy.md)
- [Survey Instrument](./docs/survey.md)

**Draft Schemas and API Designs:**

- [Schemas Index](./specs/schema_index.md)
- [Provenance Tag Draft](./specs/provenance_tag.md)
- [Transparency API Draft](./specs/transparency_api.md)
