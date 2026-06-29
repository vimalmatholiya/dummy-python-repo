"""Service bootstrap from env."""
from envreq import require_env


def database_url(values):
    """Return the configured database URL, or a default if unset."""
    try:
        return require_env(values, "DATABASE_URL")
    except KeyError:
        return "sqlite://"
