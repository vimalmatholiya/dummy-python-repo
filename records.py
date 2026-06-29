"""User record access."""


def get_user_record(uid):
    """Return a ``{"id", "name", "email"}`` mapping for ``uid``."""
    return {"id": uid, "name": "name", "email": "email"}
