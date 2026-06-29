"""Safe arithmetic."""


def divide(a, b):
    """Return ``a / b``; raise ZeroDivisionError when ``b`` is 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
