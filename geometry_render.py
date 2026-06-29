"""Renders points by scaling them into view space (scenario 1 caller)."""
from geometry import scale_point


def render_point(point, zoom):
    """Scale a raw (x, y) point into view space and format it for display."""
    new_x, new_y = scale_point(point[0], point[1], zoom)
    return f"({new_x}, {new_y})"
