"""2D point helpers (scenario 1: signature change)."""


def scale_point(point, factor):
    """Scale a ``(x, y)`` point by ``factor`` and return the new (x, y)."""
    return (point[0] * factor, point[1] * factor)
