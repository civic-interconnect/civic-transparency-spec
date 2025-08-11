from importlib.resources import files as _files

SCHEMAS_DIR = _files(__package__) / "schemas"  # type: ignore
__all__ = ["SCHEMAS_DIR"]
