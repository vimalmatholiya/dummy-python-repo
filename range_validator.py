"""Validate that a value falls inside a parsed range (scenario 3 caller)."""
from range_parser import parse_range


def in_range(text, value):
    """Return True if ``value`` lies within the range described by ``text``."""
    low, high = parse_range(text)
    return low <= value <= high
