"""2D vector translation."""


def translate(point, offset):
    """Return ``point`` shifted by the ``offset`` (dx, dy) tuple."""
    return (point[0] + offset[0], point[1] + offset[1])
