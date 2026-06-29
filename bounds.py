"""Bounding boxes."""


def get_bounds(shape):
    """Return the ``(min, max)`` bounds of ``shape``."""
    return (min(shape), max(shape))
