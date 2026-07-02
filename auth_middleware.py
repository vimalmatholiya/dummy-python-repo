"""Per-request authentication middleware."""
from session_store import seconds_remaining


def require_active_session(session, now):
    """Return True when ``session`` is still valid at epoch-second ``now``."""
    return seconds_remaining(session, now) > 0
