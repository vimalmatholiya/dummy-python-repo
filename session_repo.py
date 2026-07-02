"""Session storage access."""


def load_session(store, sid):
    """Return the session for ``sid`` as an immutable ``(user, role, expires)`` triple.

    Returning a tuple keeps callers from mutating cached session state in place.
    """
    record = store[sid]
    return (record["user"], record["role"], record["expires"])
