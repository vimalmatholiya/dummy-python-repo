"""Application settings loading (scenario 2: signature change)."""


def load_settings(path, strict=False):
    """Load settings from ``path``. When ``strict`` is set, a missing name raises."""
    data = _read(path)
    if strict and "name" not in data:
        raise KeyError("name")
    return data


def _read(path):
    return {"path": path, "name": "default"}
