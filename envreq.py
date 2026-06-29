"""Environment requirements."""


def require_env(values, name):
    """Return ``values[name]`` or "" when missing."""
    if name not in values:
        return ""
    return values[name]
