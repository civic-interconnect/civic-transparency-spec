# CONTRIBUTING.md

This repo hosts the **Civic Transparency specification and schemas** under the **MIT License**.
Our goals are clarity, privacy-by-design, and low friction for collaborators.

> TL;DR: open an Issue or Discussion first for anything non-trivial, keep PRs small and focused, and please run the quick local checks below.

---

## Ways to Contribute

- **Docs**: Fix typos, clarify definitions, or improve examples in `docs/en/**`.
- **Spec**: Propose changes to the spec text, normative notes, or privacy language.
- **Schemas**: Add or adjust JSON Schemas or the OpenAPI file in `spec/schemas/`.
- **CWEs**: Contribute new transparency pitfalls by adding a file to `docs/en/docs/cwe/`.

---

## Ground Rules

- **Code of Conduct**: Be respectful and constructive. Reports: `info@civicinterconnect.org`.
- **License**: All contributions are accepted under the repo's **MIT License**.
- **Single Source of Truth**: The normative artifacts are in `spec/schemas/`. Documentation should not contradict these files.

---

## Before You Start

1. **Open an Issue or Discussion** for non-trivial changes so we can align early.
2. For **schema changes**, describe:
   - What you want to change (field, enum, constraints).
   - Why (use case, privacy impact).
   - Backward compatibility (breaking or additive).

---

## Working Locally

```bash
# Create & activate a virtual env (Mac/Linux/WSL)
python3 -m venv .venv
source .venv/bin/activate

# Create & activate a virtual env (Windows PowerShell)
py -3.11 -m venv .venv
.\.venv\Scripts\activate

# Install tools (use **python3** for Mac/Linux/WSL)
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -e ".[dev]"
pre-commit install
```

### Validating Changes

Run all checks to ensure your changes are ready for a PR:

```shell
mkdocs build
pre-commit run --all-files
pytest -q --cov --cov-report=xml
```

### Build & Verify Package Locally (Mac/Linux/WSL)

```shell
python3 -m build
unzip -l dist/*.whl | findstr /I ".schema.json"
```

### Build & Verify Package Locally (Windows PowerShell)

```shell
py -m build

Get-ChildItem dist\*.whl | ForEach-Object {
    Expand-Archive -Path $_.FullName -DestinationPath temp_wheel -Force
}
Get-ChildItem -Recurse temp_wheel -Filter *.schema.json | Select-Object FullName

Remove-Item -Recurse -Force temp_wheel
```

### Preview Docs

```shell
mkdocs serve
```

Open browser to <http://localhost:8000/civic-transparency-spec/> to view the site.

## Making Changes

### Docs (human-readable)

- Edit files under `docs/`.
- Keep field names and enums consistent with the schemas.
- Use short, concrete examples (ISO 8601 times, explicit enum values).

### Schemas (normative)

- Follow **semantic versioning** when making changes:
  - **MAJOR**: breaking changes
  - **MINOR**: backwards-compatible additions
  - **PATCH**: clarifications/typos
- If schemas change, update the relevant docs, examples, and CHANGELOG.md.

### CWEs

- Add new entries under `docs/en/docs/cwe/` as `CWE-T0xx.md`.
- Keep the **Description / Potential Impact / Detection / Mitigation** format.
- Link it in `docs/en/docs/cwe/README.md`.

---

## Commit & PR guidelines

- **Small PRs**: one focused change per PR (easier to review).
- **Titles**: start with area, e.g., `schema: add origin_hint enum`, `docs: clarify burst_score`.
- **Link** the Issue/Discussion when applicable.
- Prefer **squash merging** for a clean history.
- No DCO/CLA required.

---

## Release process (lightweight)

1. Update `CHANGELOG.md` with notable changes.
2. Update `src/ci/transparency/spec/schemas/transparency_api.openapi.yaml` with the coming version.
3. Ensure all CI checks pass.
4. Build & verify package locally
5. Tag a new release using `git tag vx.y.z` and `git push origin vx.y.z`.
6. Create a GitHub release.

```shell
# Make sure everything is committed
git add -A
git commit -m "Prep release vx.y.z"   # as needed
git push

# Example Tag and push (setuptools_scm will use this)
git tag vx.y.z -m "x.y.z"
git push origin vx.y.z

gh release create vx.y.z --target main --title "vx.y.z" --notes "Major/Minor/Patch (pick one): describe_it_here. See CHANGELOG."

# Attach build artifacts
gh release upload vx.y.z dist/*
```

## GitHub Actions will publish to PyPI and deploy versioned docs.

## Questions / Support

- **Discussion:** For open-ended design questions.
- **Issue:** For concrete bugs or proposed text/schema changes.
- **Private contact:** `info@civicinterconnect.org` (for sensitive reports).
