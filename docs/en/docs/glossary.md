# Glossary

**acct_age_bucket**  
Broad range representing the account’s creation date relative to the post time.
Example: `0-7d`, `8-30d`, `1-6m`, `6-24m`, `24m+`.

**Adobe Content Credentials**  
Ecosystem implementing the Coalition for Content Provenance and Authenticity (C2PA) for creators and publishers.
See <https://contentcredentials.org/>.

**Atlantic Council – Digital Forensic Research Lab (DFRLab)**  
Narrative and network investigations focused on information integrity.

**automation_flag**  
Whether posting behavior indicates automation (manual, scheduled, API client, declared bot).

**behavioral metrics**  
Aggregate measures of posting patterns (for example, burst score, synchrony index) that do not consider message content.

**burst_score**  
How much a topic’s current posting volume exceeds its trailing baseline (for example, z-score or exponentially weighted moving average anomaly).

**C2PA Specification**  
Technical standard for cryptographically verifiable media provenance (manifests, assertions, signing).
See <https://spec.c2pa.org/specifications/specifications/2.2/index.html>.

**California Consumer Privacy Act (CCPA)**  
U.S. privacy law governing consumer rights and data practices; amended by the California Privacy Rights Act (CPRA) via Proposition 24 (2020).
See <https://oag.ca.gov/privacy/ccpa>.

**client_family**  
Broad client category used to post (web, mobile, third-party API).

**Coalition for Content Provenance and Authenticity (C2PA)**  
Industry coalition (Adobe, Microsoft, BBC, and others) developing open standards for media provenance. See <https://c2pa.org/>.

**Common Weakness Enumeration (CWE)**  
Project-specific catalog of recurring implementation pitfalls that can undermine project goals. See <https://cwe.mitre.org/about/index.html>.

**Content Credentials**  
Implementation layer and user experience around C2PA for creators and platforms.

**coordination_clusters**  
Groups of accounts posting identical or near-identical content in close time proximity.

**Decidim**  
Open-source platform for participatory democracy (proposals, debates, votes).

**dedup_hash**  
Hash of normalized text or media for recycled-content detection (not an identifier).

**Digital Services Act (DSA), European Union**  
Regulatory framework with transparency obligations relevant to platform reporting and risk assessments. See <https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package>.

**General Data Protection Regulation (GDPR), European Union**  
Comprehensive EU privacy regulation. See <https://gdpr.eu/>.

**Graphika**  
Network analysis firm mapping coordinated online behavior. See <https://graphika.com/>.

**Institute of Electrical and Electronics Engineers (IEEE)**  
Professional association and standards body.

**International Organization for Standardization (ISO)**  
International standards body.

**JSON Schema**  
Machine-readable schema language used here to define `series`, `meta`, `run`, `scenario`, and `provenance_tag`.

**k-anonymity**  
Privacy guarantee: no metric is published unless it represents at least *k* distinct accounts.

**Meedan**  
Open-source verification tools and training for journalists and communities.
focus on workflows and annotations.
See <https://meedan.com/>.

**Observatory on Social Media (OSoMe), Indiana University**  
Research group behind Botometer and Hoaxy; studies online manipulation and coordination.
See <https://osome.iu.edu/>.

**OpenAPI Specification (OAS)**  
Interface definition language for HTTP APIs; planned for the Transparency API reference.
See <https://www.openapis.org/>.

**post_kind**  
Type of post (original, reshare, quote, reply).

**provenance tag**  
Per-post machine-readable metadata (bucketed, non-identifying) used to compute transparency metrics.

**recycled_content_rate**  
Share of posts whose `dedup_hash` repeats more than *N* times in *M* minutes.

**Special Interest Group on Computer Science Education (SIGCSE), ACM**  
Community and conference for CS education research (for dissemination and evaluation in classrooms).

**Starling Lab**  
Research lab (Stanford and USC Shoah Foundation) advancing cryptographic provenance for media integrity. See <https://starlinglab.org/>.

**synchrony_index**  
Proportion of posts landing in unusually tight inter-arrival bins from distinct accounts.

**System and Organization Controls 2 (SOC 2)**  
Audit framework for controls related to security, availability, processing integrity, confidentiality, and privacy (a model for transparency conformance attestations).
See <https://www.aicpa.org/resources/article/what-is-soc-2>.

**window**  
Fixed time period for metric computation (for example, 1 minute, 15 minutes).
