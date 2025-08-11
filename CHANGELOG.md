# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**  
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

### Added
- (placeholder) Notes for the next release.

---

## [0.1.3] - 2025-08-10

### Fixed
- **OpenAPI/CI:** Updated release.

---

## [0.1.2] - 2025-08-10

### Changed
- **Packaging:** Adopt SPDX license string (`project.license = "MIT"`) and `project.license-files = ["LICENSE*"]`.  
- **Packaging:** Trim **sdist** using `MANIFEST.in` (exclude `.github/`, `docs/`, `site/`, `tests/`, etc.); **wheel** continues to include only package + schemas.
- **Packaging:** Ensure schema assets are bundled via `tool.setuptools.package-data` (`schemas/*.json`, `schemas/*.yaml`).
- **Build:** Bump `build-system` to `setuptools>=77` and keep `setuptools-scm[toml]>=8`.  

### Fixed
- **CI:** Harden validation to be fully offline:
  - Enforce **non-network** `$id` in all schemas.
  - OpenAPI validator locates the spec locally and resolves **relative** `$ref`s.
- **CI:** Remove Codecov upload to due to external calls/cost.

> Note: No schema shape changes.

---

## [0.1.1] - 2025-08-10

### Fixed
- **OpenAPI/CI:** Use non-network $id in schemas.

---

## [0.1.0] - 2025-08-10

### Changed
- **Schemas:** Switched all `$ref` links to **relative paths** so CI validates offline and does not rely on the docs site being published.
- **Schemas:** Small validation polish (descriptions/examples, consistent probability helper, `minProperties` on distributions). Stricter validation may surface edge cases.

### Fixed
- **OpenAPI/CI:** Local ref resolution for the `SeriesDoc` in `transparency_api.openapi.yaml`.

---

## [0.0.6] - 2025-08-10

### Fixed
- **CI:** Updated schema URLs used by validation scripts.

---

## [0.0.5] - 2025-08-10

### Fixed
- **CI:** Corrected OpenAPI path used during validation.

---

## [0.0.4] - 2025-08-10

### Fixed
- **Docs:** Correct docs base URL to `civic-transparency-spec`.

---

## [0.0.3] - 2025-08-10

### Changed
- **README:** Added `pip install` instructions and a Python quick-start validation example.

### Added
- **CHANGELOG.md:** Initial content.

---

## [0.0.2] - 2025-08-10

### Added
- **Docs:** "All-in-One" integrated page (`docs/en/docs/all.md`) using `mkdocs-include-markdown-plugin`.
- **Docs:** "Last updated" footer via `git-revision-date-localized-plugin` with ISO date format (`YYYY-MM-DD`).
- **CI/CD:** Tag-driven release workflow (`.github/workflows/release.yml`) with:
  - PyPI **Trusted Publishing** (OIDC) for automated package releases.
  - Versioned docs deploy via **mike** (`gh-pages`) and `latest` alias update.
- **CI:** PR/branch CI (`.github/workflows/ci.yml`) with pip caching, lint/tests, schema & OpenAPI validation, and doc build sanity check.
- **Packaging:** `MANIFEST.in` to include JSON schemas in **sdist** in addition to wheel.

### Changed
- **Schemas:** De-duplicated enums via `$defs` in `provenance_tag.schema.json` and referenced from `series.schema.json`.
- **Docs:** Sidebar/nav cleanup; fixed include paths relative to `docs_dir: docs/en`.
- **README:** Added usage instructions and example.

### Fixed
- **Schemas:** Trailing quote typo and cross-ref cleanup in `provenance_tag.schema.json`.
- **MkDocs:** Removed native PDF plugin locally (WeasyPrint/GTK issue on Windows); can re-enable in CI later.

---

## [0.0.1] - 2025-08-10

### Added
- Initial public release of **Civic Transparency specification schemas** (JSON Schema Draft-07):
  - `meta.schema.json`, `provenance_tag.schema.json`, `run.schema.json`, `scenario.schema.json`, `series.schema.json`
- **OpenAPI 3.1**: `transparency_api.openapi.yaml`
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

[Unreleased]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.1.2...HEAD  
[0.1.2]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.1.1...v0.1.2  
[0.1.1]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.6...v0.1.0
[0.0.6]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/civic-interconnect/civic-transparency-spec/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/civic-interconnect/civic-transparency-spec/releases/tag/v0.0.1
