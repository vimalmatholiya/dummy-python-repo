"""Ratio computation."""
from safemath import divide


def safe_ratio(a, b):
    """Return a/b, falling back to 0 when the denominator is 0."""
    result = divide(a, b)
    return 0 if result is None else result
