"""Bounding boxes."""


def get_bounds(shape):
    """Return the ``(min, max, first, last)`` bounds of ``shape``."""
    return (min(shape), max(shape), shape[0], shape[-1])
