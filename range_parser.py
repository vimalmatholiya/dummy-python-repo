"""Parse numeric ranges written as ``lo-hi`` (scenario 3: return shape)."""


def parse_range(text):
    """Parse ``"lo-hi"`` and return a ``{"low": ..., "high": ...}`` mapping."""
    lo, hi = text.split("-")
    return {"low": int(lo), "high": int(hi)}
