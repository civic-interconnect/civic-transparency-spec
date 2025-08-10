# Civic Transparency

> **Verified Provenance & Behavior Transparency Standard**  
> An open, nonpartisan specification for privacy-preserving visibility into how content spreads online.

- [GitHub Source Repository](https://github.com/civic-interconnect/civic-transparency-spec)
- [Hosted Documentation](https://civic-interconnect.github.io/civic-transparency-spec/)

Official documentation for the Civic Transparency project.

---

## Vision

Create a low-cost, behavioral early-warning dashboard by:

- Ingesting publicly available, ToS-compliant data from platforms with usable APIs.
- Tracking bursts, synchrony, recycled media, and sudden follower spikes without assessing message content.
- Publishing aggregated event-level signals (e.g., _High coordination spike on Platform X in Topic Y_) instead of targeting individuals.
- Providing toolkits for journalists, civic groups, and election officials to investigate further.

---

## Motivation

Coordinated manipulation thrives when people can't see how narratives spread or whether automation is involved.

We do **not** judge truth or police viewpoints.  
Instead, we show how content moves (provenance and behavior) so everyone can evaluate trends on equal footing.

For platform providers, the system uses **low-cost metadata** and aggregated signals, reducing legal risk and operational burden.

---

## Proposal

1. Platforms embed **machine-readable provenance tags** in every public post:
   - Account creation date bucket
   - Automation flag
   - Original vs. reshared
   - Media provenance (if available)
2. Platforms host a **public transparency endpoint** (low-cost API) that returns aggregate counts of behavior types for a given hashtag, topic, or trend.
3. Personal accounts are protected:
   - Broad date ranges instead of exact creation dates
   - No personal identifiers
   - Privacy by design

---

## Benefits for Platforms

- **Reduced liability.** Transparency data shifts blame to bad actors if manipulation is uncovered.
- **Trust & brand boost.** Visible commitment to transparency.
- **Lower moderation costs.** Third parties help detect automation.
- **Compliance ready.** Aligns with EU DSA and other transparency laws.

---

## Benefits for People

- **Easy public verification.** Check how organic a trend is.
- **Less disinformation amplification.** Mass coordination is harder to hide.
- **User choice.** Users can filter feeds based on automation or coordination scores.

---

## Core Design Principles

- **Provenance tags** at post creation.
- **Aggregated behavioral stats** via public API.
- **Privacy by design.** Use bucketed/ranged values, no personal data, no DMs, no full content export.

---

## Key Aspects

1. Spot abnormal account-age skews.
2. Flag synchrony spikes and recycled-content bursts without identifying individuals.
3. Compare automation rates across topics and dates.
4. Enforce privacy safeguards. Use buckets only, no join keys.
5. Publish only aggregated outputs (e.g., k-anonymity ≥ 100).
6. Keep metrics behavioral, not ideological.
7. Allow appeals & audits.
8. Document methods openly.

## Costs & Incentives

- **Low compute cost.** Tags set once; aggregation uses compact counters.
- **Scalable delivery.** Caching and rate limits for popular queries.
- **Legal risk reduction.** Transparent, standardized outputs.
- **Trust dividend.** Benefits regulators, advertisers, and users.
- **Global fit.** Aligns with transparency mandates like the EU DSA.

## Governance & standardization

- **Neutral steward.** Multi-stakeholder working group.
- **Versioned spec & model cards.** Changes documented; platforms publish transparency model cards.
- **Certification tier.** Offer independent audits, SOC 2-style.

---

## Visibility Boundaries

**Reveals:** Coordination patterns, automation mix, recycled media rates, account-age skews, provenance quality signals.

**Does NOT reveal:** Exact identities, private messages, sensitive client info, individual posts, or "truth."

---

## Risks & Mitigations

- **Actors adapt:** They can age accounts longer.

  - Mitigation: evaluate multiple complementary signals.

- **Topic gaming:** Flood benign posts under a hashtag.

  - Mitigation: multi-query by URL/media hash and anomaly comparison.

- **Chilling concerns:** Users fear being "scored."

  - Mitigation: only aggregates are public; tags used for computation only.

- **Platform under-implementation:**
  - Mitigation: offer certification and provide public conformity reports.

## Success metrics

- **Short term:** watchdogs and journalists cite coordination metrics in coverage.
- **Medium term:** fewer high-risk patterns during elections without suppressing organic growth.
- **Long term:** higher trust metrics and cross-platform adoption.

---

## Implementation Plan

1. Develop and test on simulated data via GitHub Pages.
2. Prototype on open platforms (BlueSky, Fediverse, Reddit).
3. Publish standard + open-source reference implementation.
4. Pilot on low-stakes topics (sports, entertainment).
5. Independent audits for fairness and privacy protection.
6. Engage regulators with cost/benefit evidence.

---

## Read More

- [Glossary](./docs/glossary.md)
- [Governance](./docs/governance.md)
- [Metrics](./docs/metrics.md)
- [Privacy](./docs/privacy.md)
- [Survey](./docs/survey.md)

**Specifications:**

- [Schemas](./specs/schema_index.md)
- [Provenance Tag](./specs/provenance_tag.md)
- [Transparency API](./specs/transparency_api.md)
