# Schema Index (Normative Artifacts)

This page lists the **canonical, machine-readable schemas** for Civic Transparency.
Human-readable explanations live in:
- [Provenance Tag](./provenance_tag.md) *(informative)*
- [Transparency API](./transparency_api.md) *(informative)*

## Guidelines

The schema design emphasizes:
- **Behavior-only focus**: No message content storage.
- **Privacy preservation**: All values are bucketed or aggregated.
- **Extensibility**: Allows adding new metrics or buckets without breaking existing consumers.

## JSON Schema (Draft-07)

- **SeriesDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/series.schema.json`  
  File: `spec/schemas/series.schema.json`

- **MetaDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/meta.schema.json`  
  File: `spec/schemas/meta.schema.json`

- **RunDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/run.schema.json`  
  File: `spec/schemas/run.schema.json`

- **Provenance Tag**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/provenance_tag.schema.json`  
  File: `spec/schemas/provenance_tag.schema.json`

## OpenAPI (HTTP Interface)

- **Transparency API**  
  File: `spec/schemas/transparency_api.openapi.yaml`  
  Response bodies **MUST** validate against the JSON Schemas above.

## Versioning & Conformance

- Schemas use **semantic versioning**.  
  - MAJOR = breaking, MINOR = additive, PATCH = clarifications.  
- Implementers **MUST** pin to a specific schema version and validate.  
- Deprecations are announced in `CHANGELOG.md` and tagged releases.

## Code Generation (informative)

For typed clients, we recommend generating models from the JSON Schemas.

```bash
# Example (Python / pydantic) – run in your own repo:
datamodel-code-generator \
  --input spec/schemas/series.schema.json \
  --input-file-type jsonschema \
  --output src/ci/transparency/types/series.py
```

## Provenance & Privacy Notes (pointers)

- Buckets, not PII; behavior-only signals.  
- Minimum group size (e.g., **k ≥ 100**) enforced at the API.  
See [Privacy](../docs/privacy.md) for policy details.
