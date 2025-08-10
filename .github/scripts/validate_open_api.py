# .github/scripts/validate_open_api.py
from pathlib import Path
import sys

# Prefer validate_spec if available; fall back to validate()
try:
    from openapi_spec_validator import validate_spec as _validate
except Exception:  # older versions
    from openapi_spec_validator import validate as _validate  # type: ignore

from openapi_spec_validator.readers import read_from_filename

ROOT = Path(__file__).resolve().parents[2]

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
