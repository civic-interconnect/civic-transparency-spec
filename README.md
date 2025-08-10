# Civic Transparency – Specifications

[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)](https://civic-interconnect.github.io/civic-transparency-spec/)
[![PyPI](https://img.shields.io/pypi/v/civic-transparency-spec.svg)](https://pypi.org/project/civic-transparency-spec/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python)](#)
[![CI Status](https://github.com/civic-interconnect/civic-transparency-spec/actions/workflows/ci.yml/badge.svg?branch=main
)](https://github.com/civic-interconnect/civic-transparency-spec/actions/workflows/ci.yml)
[![JSON Schema: Draft-07](https://img.shields.io/badge/JSON%20Schema-Draft--07-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> **Verified Provenance & Behavior Transparency Standard**

> Civic Transparency is an open specification for privacy-preserving, non-partisan visibility into how content spreads online.
> It defines machine-readable provenance tags and aggregated behavioral metrics that platforms can expose via a low-cost API, enabling journalists, watchdogs, and civic groups to detect coordination patterns and automation without exposing personal data or judging content.

> Maintained by **[Civic Interconnect](https://github.com/civic-interconnect)**.

- [Documentation](https://civic-interconnect.github.io/civic-transparency-spec/)
- [Schemas](./specs/schema_index.md)
- [Contributing](./CONTRIBUTING.md)

---

## Install

```bash
pip install civic-transparency-spec
```

---

## Install (Unpinned or Pinned Version)

Choose one:

```bash
pip install civic-transparency-spec
pip install civic-transparency-spec==0.0.2
```

## Quick start (validate with JSON Schema)

The package ships the normative Draft-07 schemas.
Load them from the package and validate your data:

```python
from importlib.resources import files
import json
from jsonschema import Draft7Validator

# Load a schema (SeriesDoc shown here). Available files:
#   meta.schema.json, provenance_tag.schema.json, run.schema.json, scenario.schema.json, series.schema.json
schema_text = files("ci.transparency.spec.schemas").joinpath("series.schema.json").read_text(encoding="utf-8")
series_schema = json.loads(schema_text)

# Validate your payload (raises jsonschema.ValidationError if invalid)
Draft7Validator.check_schema(series_schema)  # optional: sanity check the schema itself
payload = {
    "topic": "#CityElection2026",
    "generated_at": "2026-02-07T00:00:00Z",
    "interval": "minute",
    "points": []
}
Draft7Validator(series_schema).validate(payload)
print("Success: Valid SeriesDoc")
```

List all bundled schemas:

```python
from importlib.resources import files
print([p.name for p in files("ci.transparency.spec.schemas").iterdir()])
```

## OpenAPI

The HTTP interface is documented on the docs site.
Response bodies should validate against the JSON Schemas above.  
See: [Transparency API](https://civic-interconnect.github.io/civic-transparency-spec/specs/transparency_api/)

## Notes

- Target Python: **3.11** (CI runs on 3.11).
- Schemas: **JSON Schema Draft-07**; OpenAPI: **3.1**.
- This repo is a **specification**; the primary artifacts are schemas + documentation.

---

## Project Organization

## Project layout & where to find things

```text
civic-transparency-spec/
├─ .github/workflows/             # CI, release, docs
├─ docs/
│  └─ en/
│     ├─ index.md                 # docs homepage
│     ├─ docs/                    # narrative docs
│     │  ├─ all.md                # integrated 1-pager
│     │  ├─ glossary.md
│     │  ├─ governance.md
│     │  ├─ metrics.md
│     │  ├─ privacy.md
│     │  └─ survey.md
│     └─ specs/                   # spec explainer pages
│        ├─ provenance_tag.md
│        ├─ schema_index.md
│        └─ transparency_api.md
├─ src/
│  └─ ci/transparency/spec/
│     ├─ __init__.py
│     └─ schemas/                 # canonical JSON Schemas + OpenAPI (shipped in the wheel)
│        ├─ meta.schema.json
│        ├─ provenance_tag.schema.json
│        ├─ run.schema.json
│        ├─ scenario.schema.json
│        ├─ series.schema.json
│        └─ transparency_api.openapi.yaml
├─ tests/                         # schema + OpenAPI validation tests
├─ mkdocs.yml                     # Set up MkDocs
└─ pyproject.toml                 # packaging config (schemas included via package-data)


---

## About

Civic Transparency is an open specification for privacy-preserving, non-partisan visibility into **how** content spreads online (not what it says). 
