"""Session storage access."""


def load_session(store, sid):
    """Return the session record for ``sid`` as ``{user, role, expires}``."""
    return store[sid]
