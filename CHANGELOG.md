# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**  
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

### Added

- (placeholder) Add notes here for the next release.

---

## [0.0.3] - 2025-08-10

### Changed

- **CHANGELOG.md:** Added initial content.
- **README:** Added `pip install` instructions and a Python quick-start validation example.

---

## [0.0.2] - 2025-08-10

### Added

- **Docs:** “All-in-One” integrated page (`docs/en/docs/all.md`) using `mkdocs-include-markdown-plugin`.
- **Docs:** “Last updated” footer via `git-revision-date-localized-plugin` with ISO date format (`YYYY-MM-DD`).
- **CI/CD:** Tag-driven release workflow (`.github/workflows/release.yml`) with:
  - PyPI **Trusted Publishing** (OIDC) for automated package releases.
  - Versioned docs deploy via **mike** (`gh-pages`) and `latest` alias update.
- **CI:** Modernized PR/branch CI (`.github/workflows/ci.yml`) with pip caching, lint/tests, schema and OpenAPI validation, and doc build sanity check.
- **Packaging:** `MANIFEST.in` to include JSON schemas in **sdist** in addition to wheel.

### Changed

- **Schemas:** `provenance_tag.schema.json` now defines enums once under `$defs` and is referenced from `series.schema.json` to avoid duplication.
- **Docs:** Sidebar/nav cleanup; fixed include paths relative to `docs_dir: docs/en`.
- **README:** Added `pip install` instructions and a Python quick-start validation example.

### Fixed

- **Schemas:** Trailing quote typo in `provenance_tag.schema.json` and cross-ref cleanup.
- **MkDocs:** Removed native PDF plugin locally (WeasyPrint/GTK issue on Windows); can re-enable via CI if needed.

---

## [0.0.1] - 2025-08-10

### Added

- Initial public release of **Civic Transparency specification schemas** (JSON Schema Draft-07):
  - `meta.schema.json`, `provenance_tag.schema.json`, `run.schema.json`, `scenario.schema.json`, `series.schema.json`
- **OpenAPI 3.1** file: `transparency_api.openapi.yaml`
- **Docs site** scaffolding (MkDocs Material, i18n).
- **Testing:** Basic schema/OpenAPI validation tests; Ruff lint; pre-commit hooks.
- **Packaging:** Wheel includes schema files via `tool.setuptools.package-data`.

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking schema/OpenAPI changes
  - **MINOR** – backward-compatible additions
  - **PATCH** – clarifications, docs, tooling
- Versions are driven by git tags via `setuptools_scm`. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

[Unreleased]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.3...HEAD
[0.0.3]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/civic-interconnect/civic-transparency-spec/releases/tag/v0.0.1
