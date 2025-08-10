# tests/test_config.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repo root
SRC_SCHEMAS = ROOT / "src" / "ci" / "transparency" / "spec" / "schemas"
LEGACY_SCHEMAS = ROOT / "spec" / "schemas"


def any_schema_dir():
    # prefer packaged location; fall back to legacy if present
    for p in (SRC_SCHEMAS, LEGACY_SCHEMAS):
        if p.is_dir():
            return p
    raise RuntimeError(f"No schema dir found. Tried: {SRC_SCHEMAS}, {LEGACY_SCHEMAS}")
