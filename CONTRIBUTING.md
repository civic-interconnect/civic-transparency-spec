# CONTRIBUTING.md

This repo hosts the **Civic Transparency specification and schemas** under the **MIT License**.
Our goals are clarity, privacy-by-design, and low friction for collaborators.

> tl;dr: open an Issue or Discussion first for anything non-trivial, keep PRs small and focused, and please run the quick local checks below.

---

## Ways to Contribute

- **Docs**: Fix typos, clarify definitions, or improve examples in `docs/en/**`.
- **Spec**: Propose changes to the spec text, normative notes, or privacy language.
- **Schemas**: Add or adjust JSON Schemas or the OpenAPI file in `src/ci/transparency/spec/schemas/`.
- **CWEs**: Contribute new transparency pitfalls under `docs/en/docs/cwe/`.

---

## Ground Rules

- **Code of Conduct**: Be respectful and constructive. Reports: `info@civicinterconnect.org`.
- **License**: All contributions are accepted under the repo's **MIT License**.
- **Single Source of Truth**: The normative artifacts are in `src/ci/transparency/spec/schemas/`. Documentation should not contradict these files.

---

## Before You Start

1. **Open an Issue or Discussion** for non-trivial changes so we can align early.
2. For **schema changes**, describe:

- What you want to change (field, enum, constraints).
- Why (use case, privacy impact).
- Backward compatibility (breaking or additive).

---

## Making Changes

### Docs (human-readable)

- Edit files under `docs/`.
- Keep field names and enums consistent with the schemas.
- Use short, concrete examples (ISO 8601 times, explicit enum values).

### Schemas (normative)

- Follow **Semantic Versioning**:
  - **MAJOR**: breaking changes
  - **MINOR**: backwards-compatible additions
  - **PATCH**: clarifications/typos
- If schemas change, update related docs, examples, and `CHANGELOG.md`.

### CWEs

- Add entries under `docs/en/docs/cwe/` as `CWE-T0xx.md`.
- Keep **Description / Potential Impact / Detection / Mitigation** format.
- Link it in `docs/en/docs/cwe/README.md`.

---

## Commit & PR guidelines

- **Small PRs**: one focused change per PR.
- **Titles**: start with area, e.g., `schema: add origin_hint enum`, `docs: clarify burst_score`.
- **Link** the Issue/Discussion when applicable.
- Prefer **squash merging** for a clean history.
- No DCO/CLA required.

---

## Questions / Support

- **Discussion:** For open-ended design questions.
- **Issue:** For concrete bugs or proposed text/schema changes.
- **Private contact:** `info@civicinterconnect.org` (for sensitive reports).

---

## DEV 1. Start Locally

**Mac/Linux/WSL**

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -e ".[dev]"
pre-commit install
```

**Windows (PowerShell)**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install -e ".[dev]"
pre-commit install
```

## DEV 2. Validate Changes

Run all checks.

````shell
mkdocs build
pre-commit run --all-files
pytest -q

## DEV 3. Preview Docs

```bash
mkdocs serve
````

Open: <http://127.0.0.1:8000/>

## DEV 4. Release

1. Update `CHANGELOG.md` with notable changes.
2. Update `src/ci/transparency/spec/schemas/transparency_api.openapi.yaml` with the coming version.
3. Ensure all CI checks pass.
4. Build & verify package locally.
5. Tag and push (setuptools_scm uses the tag).

```bash
git add .
git commit -m "Prep vx.y.z"
git push origin main

git tag vx.y.z -m "x.y.z"
git push origin vx.y.z
```

> A GitHub Action will **build**, **publish to PyPI** (Trusted Publishing), **create a GitHub Release** with artifacts, and **deploy versioned docs** with `mike`.

> You do **not** need to run `gh release create` or upload files manually.
