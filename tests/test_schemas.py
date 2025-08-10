# tests/test_schemas.py
from __future__ import annotations

import json
import re
from pathlib import Path
import pytest
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIRS = [
    ROOT / "src" / "ci" / "transparency" / "spec" / "schemas",
    ROOT / "spec" / "schemas",  # legacy fallback if you ever move back
]


def iter_schema_files() -> list[Path]:
    files: list[Path] = []
    for d in SCHEMA_DIRS:
        if d.is_dir():
            files.extend(sorted(d.glob("*.schema.json")))
    if not files:
        raise RuntimeError(
            f"No schema files found in: {', '.join(map(str, SCHEMA_DIRS))}"
        )
    return files


@pytest.mark.parametrize("path", iter_schema_files())
def test_schema_is_valid_draft7_and_offline(path: Path) -> None:
    with path.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    # Guard: avoid http(s) $id which can trigger remote fetch in validators
    sid = schema.get("$id", "")
    assert not re.match(r"^https?://", sid), f"{path} uses network $id: {sid}"

    # Structure must be a valid Draft-07 schema
    Draft7Validator.check_schema(schema)


def test_expected_files_present() -> None:
    names = {p.name for p in iter_schema_files()}
    expected = {
        "meta.schema.json",
        "provenance_tag.schema.json",
        "run.schema.json",
        "scenario.schema.json",
        "series.schema.json",
    }
    missing = expected - names
    assert not missing, f"Missing schemas: {sorted(missing)}"
