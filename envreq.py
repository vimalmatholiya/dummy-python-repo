"""Environment requirements."""


def require_env(values, name):
    """Return ``values[name]`` or raise KeyError when missing."""
    if name not in values:
        raise KeyError(name)
    return values[name]
