# About Specs: Provenance Tag

> **Status:** Human-readable overview.  
> **Normative definition:** See the JSON Schema at  
> `spec/schemas/provenance_tag.schema.json`  
> (`$id: https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/provenance_tag.schema.json`)

Added to public posts (stored server-side for aggregate queries; not shown per-user unless a platform chooses to).

**Fields (bucketed / coarse):**
- `acct_age_bucket` — e.g., `0-7d`, `8-30d`, `1-6m`, `6-24m`, `24m+`
- `acct_type` — `person`, `org`, `media`, `public_official`, `unverified` (optional: `declared_automation`)
- `automation_flag` — `manual`, `scheduled`, `api_client`, `declared_bot` (self-labeled)
- `post_kind` — `original`, `reshare`, `quote`, `reply`
- `client_family` — `web`, `mobile`, `third_party_api` (no specific app IDs)
- `media_provenance` — `c2pa_present`, `hash_only`, `none`
- `origin_hint` — coarse locale bucket (country/region), **only where lawful**
- `dedup_hash` — rolling/normalized hash for identical/near-identical text/media

**Privacy & neutrality**
- Bucketed categories only; no handles, PII, or message content.  
- Used to compute **aggregate** transparency metrics (not to score individuals).

**Conformance & stability**
- Implementations **MUST** validate against the JSON Schema.  
- Changes follow semver; breaking changes bump the schema’s **MAJOR**.
- Platforms **SHOULD** publish method notes describing how they populate each field.

**Non-normative example**
```json
{
  "acct_age_bucket": "1-6m",
  "acct_type": "person",
  "automation_flag": "scheduled",
  "post_kind": "reshare",
  "client_family": "mobile",
  "media_provenance": "c2pa_present",
  "origin_hint": "EU",
  "dedup_hash": "rhh_6f4c…"
}
```