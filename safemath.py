"""Safe arithmetic."""


def divide(a, b):
    """Return ``a / b``, or None when ``b`` is 0."""
    if b == 0:
        return None
    return a / b
