"""Session bootstrap."""
from auth import make_token


def open_session(user_id):
    """Mint a 1-hour token for ``user_id``."""
    return make_token(user_id, 3600)
