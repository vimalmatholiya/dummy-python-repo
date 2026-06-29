"""Ratio computation."""
from safemath import divide


def safe_ratio(a, b):
    """Return a/b, falling back to 0 when the denominator is 0."""
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return 0
