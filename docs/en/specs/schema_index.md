# Schema Index (Draft / Normative Artifacts)

This page lists **draft machine-readable schemas** for the Civic Transparency specification.

Human-readable explanations live in:
- [Provenance Tag](./provenance_tag.md) *(informative)*
- [Transparency API](./transparency_api.md) *(informative)*

---

## Design Goals

These schemas prioritize:
- **Behavior-only scope** – no message content or identifiers.
- **Privacy preservation** – bucketed values and k-anonymity safeguards.
- **Forward compatibility** – extensible formats with stable IDs.

---

## JSON Schema (Draft-07)

Each schema is self-contained and versioned.

- **SeriesDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/series.schema.json`  
  File: `spec/schemas/series.schema.json`

- **MetaDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/meta.schema.json`  
  File: `spec/schemas/meta.schema.json`

- **RunDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/run.schema.json`  
  File: `spec/schemas/run.schema.json`

- **ProvenanceTag**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/provenance_tag.schema.json`  
  File: `spec/schemas/provenance_tag.schema.json`

---

## OpenAPI

- **Transparency API**  
  File: `spec/schemas/transparency_api.openapi.yaml`  
  All responses **must validate** against the JSON Schemas above.

---

## Versioning & Conformance

- Schemas follow **semantic versioning**:  
  - MAJOR = breaking  
  - MINOR = additive  
  - PATCH = clarifying
- Clients **must pin** to a specific version and validate before ingesting.
- Changes and deprecations are documented in `CHANGELOG.md`.

---

## Code Generation (informative)

You can generate typed clients from the JSON Schemas.

```bash
# Example (Python + Pydantic)
datamodel-code-generator \
  --input spec/schemas/series.schema.json \
  --input-file-type jsonschema \
  --output src/ci/transparency/types/series.py
```

## Provenance & Privacy Notes

- **Signals only**: All values are behavioral, not textual.
- **Minimum group size**: Enforced at the API layer (e.g., `k ≥ 100`).
- **PII-free by design**: See [Privacy](../docs/privacy.md) for details.
