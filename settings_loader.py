"""Application settings loading (scenario 2: signature change)."""


def load_settings(path, raise_on_missing=False):
    """Load settings from ``path``. When ``raise_on_missing`` is set, a missing name raises."""
    data = _read(path)
    if raise_on_missing and "name" not in data:
        raise KeyError("name")
    return data


def _read(path):
    return {"path": path, "name": "default"}
