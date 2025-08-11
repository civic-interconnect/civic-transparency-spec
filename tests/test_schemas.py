# tests/test_schemas.py
from __future__ import annotations

import json
from importlib.resources import files
from typing import Iterable, Any
from jsonschema import Draft7Validator
from ci.transparency import spec # ensure package is imported for coverage


def _schema_paths() -> Iterable[str]:
    pkg = files("ci.transparency.spec.schemas")
    for name in (
        "meta.schema.json",
        "provenance_tag.schema.json",
        "run.schema.json",
        "scenario.schema.json",
        "series.schema.json",
    ):
        yield str(pkg.joinpath(name))

def test_package_imports_for_coverage():
    res: Any = spec
    assert res is not None  # touches the object for ruff

def test_json_schemas_are_valid() -> None:
    for schema_path in _schema_paths():
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        # Will raise if invalid
        Draft7Validator.check_schema(schema)
