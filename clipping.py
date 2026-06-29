"""Viewport clipping."""
from bounds import get_bounds


def span(shape):
    """Return the size of ``shape``'s bounding span."""
    low, high = get_bounds(shape)
    return high - low
