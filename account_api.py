"""Account profile API (out-of-diff caller of session_repo.load_session)."""
from session_repo import load_session


def current_username(store, sid):
    """Return the display name for the account behind session ``sid``."""
    return load_session(store, sid)["user"]
