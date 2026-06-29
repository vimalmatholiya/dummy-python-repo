"""Parse numeric ranges written as ``lo-hi`` (scenario 3: return shape)."""


def parse_range(text):
    """Parse ``"lo-hi"`` and return the (low, high) bounds as a tuple."""
    lo, hi = text.split("-")
    return (int(lo), int(hi))
