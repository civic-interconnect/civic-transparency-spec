# tests/test_openapi.py
from __future__ import annotations

import inspect
import os
import re
from importlib.resources import as_file, files
from pathlib import Path
from typing import Any, Iterable

from openapi_spec_validator import validate as osv_validate
from openapi_spec_validator.readers import read_from_filename


def _walk_refs(node: Any) -> Iterable[str]:
    """Yield every string value under a '$ref' key (deep)."""
    if isinstance(node, dict):
        for k, v in node.items():  # type: ignore
            if k == "$ref" and isinstance(v, str):
                yield v
            else:
                yield from _walk_refs(v)
    elif isinstance(node, list):
        for item in node:  # type: ignore
            yield from _walk_refs(item)


def _uri_to_local_path(uri: str) -> Path:
    """Convert file:// URI -> local Path (Windows-safe) and print what we do."""
    from urllib.parse import urlparse, unquote

    parts = urlparse(uri)
    print(f"[uri->path] scheme={parts.scheme} uri={uri}")
    if parts.scheme != "file":
        raise AssertionError(f"Expected file:// base, got: {uri!r}")
    path = unquote(parts.path)
    # Windows quirk: file:///C:/... becomes /C:/..., strip leading slash.
    if os.name == "nt" and re.match(r"^/[A-Za-z]:", path):
        path = path[1:]
    p = Path(path)
    print(f"[uri->path] local={p} exists={p.exists()}")
    return p


def test_openapi_31_validates_offline() -> None:
    print("\n[STEP 1] Locate OpenAPI YAML from installed package resources")
    res = files("ci.transparency.spec.schemas").joinpath(
        "transparency_api.openapi.yaml"
    )
    print(f"[resource] {res!r}")

    print(
        "\n[STEP 2] Materialize resource to a real path so the validator can resolve relatives"
    )
    with as_file(res) as tmp_path:
        openapi_path = Path(tmp_path).resolve()
        print(f"[openapi path] {openapi_path} (exists={openapi_path.exists()})")
        assert openapi_path.exists(), "OpenAPI YAML not found in installed package!"

        print(
            "\n[STEP 3] Load spec with reader (yields base_uri for resolving './*.schema.json')"
        )
        spec_dict, base_uri = read_from_filename(str(openapi_path))
        print(f"[base_uri] {base_uri!r}")

        print("\n[STEP 4] Sanity—top-level fields present?")
        assert isinstance(spec_dict, dict), "spec_dict should be a dict"
        print(f"[openapi] {spec_dict.get('openapi')}")
        assert "paths" in spec_dict, "Missing 'paths' in spec"

        print("\n[STEP 5] List all $ref values")
        refs = list(_walk_refs(spec_dict))
        for r in refs:
            print(f"  $ref: {r}")
        assert refs, "No $ref found — unexpected for this spec."

        print("\n[STEP 6] Verify every relative $ref points to an existing local file")
        base_dir = _uri_to_local_path(base_uri).parent
        for r in refs:
            if r.startswith("./"):
                target = (base_dir / r).resolve()
                print(f"  -> {r} => {target} (exists={target.exists()})")
                assert target.exists(), f"Relative ref not found locally: {r}"

        print("\n[STEP 7] Show validator signature (so we KNOW what it supports)")
        sig = str(inspect.signature(osv_validate))
        print(f"[validate signature] validate{sig}")

        print(
            "\n[STEP 8] Validate offline using validate(spec_dict, base_uri=...) ONLY"
        )
        try:
            osv_validate(spec_dict, base_uri=base_uri)
        except TypeError as te:
            print("[validate] TypeError calling validate(spec_dict, base_uri=...)")
            print(f"           -> {te}")
            print(
                "           Your installed openapi-spec-validator does not accept 'base_uri'."
            )
            print(
                "           ACTION: bump 'openapi-spec-validator' to a version that supports"
            )
            print(
                "           validate(spec_dict, base_uri=...) OR change your test to pass a"
            )
            print("           validator that supports a base URI explicitly.")
            raise
        print("✅ validate(spec_dict, base_uri=...) succeeded offline")

        print(
            "\n✅ All steps passed — local refs resolved & OpenAPI validated offline."
        )


def test_relative_series_schema_exists_next_to_openapi() -> None:
    """Focused guard to catch the './series.schema.json' problem immediately."""
    res = files("ci.transparency.spec.schemas").joinpath(
        "transparency_api.openapi.yaml"
    )
    with as_file(res) as p:
        openapi_path = Path(p).resolve()
        _, base_uri = read_from_filename(str(openapi_path))
        base_dir = _uri_to_local_path(base_uri).parent
        target = (base_dir / "./series.schema.json").resolve()
        print(f"[neighbor] {target} exists={target.exists()}")
        assert target.exists(), "series.schema.json missing next to the OpenAPI file"
