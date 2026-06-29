"""Sprite movement."""
from vectors import translate


def move_right(position, step):
    """Move a sprite ``step`` pixels to the right."""
    return translate(position, step, 0)
