# .github/scripts/validate_open_api.py
from pathlib import Path
import sys
import json
import re
from typing import List, Tuple


# Prefer validate_spec if available; fall back to validate()
try:
    from openapi_spec_validator import validate_spec as _validate
except Exception:  # older versions
    from openapi_spec_validator import validate as _validate  # type: ignore

from openapi_spec_validator.readers import read_from_filename

ROOT = Path(__file__).resolve().parents[2]

# 1) Guard: ensure no schema uses http(s) $id (prevents remote fetch during validation)
SCHEMA_DIRS = [
    ROOT / "src" / "ci" / "transparency" / "spec" / "schemas",
    ROOT / "spec" / "schemas",
]

bad: List[Tuple[Path, str]] = []
for d in SCHEMA_DIRS:
    if not d.is_dir():
        continue
    for p in d.glob("*.schema.json"):
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        sid = data.get("$id", "")
        print(f"[schema] {p}: $id={sid}")
        if re.match(r"^https?://", sid):
            bad.append((p, sid))
if bad:
    print("\nERROR: Found http(s) $id values (these cause remote dereferencing):")
    for p, sid in bad:
        print(f" - {p} -> {sid}")
    sys.exit(1)
else:
    print("OK: no http(s) $id values found in schemas.")

# 2) Find OpenAPI file (src first, fallback to legacy path)
CANDIDATES = [
    ROOT / "src" / "ci" / "transparency" / "spec" / "schemas" / "transparency_api.openapi.yaml",
    ROOT / "spec" / "schemas" / "transparency_api.openapi.yaml",
]
openapi_path = next((p for p in CANDIDATES if p.is_file()), None)
if not openapi_path:
    print("OpenAPI file not found. Tried:")
    for p in CANDIDATES:
        print(f"  - {p}")
    sys.exit(1)

spec_dict, base_uri = read_from_filename(str(openapi_path))
_validate(spec_dict)
print(f"OpenAPI looks valid. ✅  ({openapi_path})")
