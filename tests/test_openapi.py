# tests/test_openapi.py
from pathlib import Path
import subprocess
import sys

# Local OpenAPI file (validate strictly offline)
SPEC_PATH = (
    Path(__file__).resolve().parents[1]
    / "src" / "ci" / "transparency" / "spec" / "schemas" / "transparency_api.openapi.yaml"
)

def test_openapi_validates_offline_cli() -> None:
    assert SPEC_PATH.is_file(), f"OpenAPI file not found: {SPEC_PATH}"

    # Use the package’s own CLI entrypoint via -m (documented by the project).
    # This ensures the validator knows the file:// base and resolves ./series.schema.json locally.
    proc = subprocess.run(
        [sys.executable, "-m", "openapi_spec_validator", str(SPEC_PATH)],
        capture_output=True,
        text=True,
    )

    if proc.returncode != 0:
        raise AssertionError(
            "OpenAPI validation failed via CLI:\n"
            f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}"
        )
