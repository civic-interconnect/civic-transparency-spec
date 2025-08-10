# .github/scripts/validate_schemas.py
import json
import sys
import glob
import pathlib
import re
from typing import List
from jsonschema import Draft7Validator

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA_DIRS = [
    ROOT / "src" / "ci" / "transparency" / "spec" / "schemas",
    ROOT / "spec" / "schemas",
]



schema_files: List[str] = []
for d in SCHEMA_DIRS:
    schema_files.extend(glob.glob(str(d / "*.schema.json")))

if not schema_files:
    print("No schema files found. Looked in:")
    for d in SCHEMA_DIRS:
        print(f"  - {d}")
    sys.exit(1)

had_error = False
for path in schema_files:
    with open(path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    # Guard: $id must not be network URL (prevents remote resolution in CI)
    sid = schema.get("$id", "")
    if re.match(r"^https?://", sid):
        print(f"ERROR: {path} uses network $id: {sid}")
        had_error = True
    # Validate schema structure
    try:
        Draft7Validator.check_schema(schema)
    except Exception as e:
        print(f"Schema invalid: {path}\n{e}\n")
        had_error = True
    else:
        print(f"OK: {path}")

if had_error:
    sys.exit(1)

print("All JSON Schemas are valid and use non-network $id values. ✅")
