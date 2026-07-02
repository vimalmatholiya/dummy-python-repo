"""Session lifecycle helpers (clock standardized on milliseconds)."""

SESSION_TTL_SECONDS = 1800 * 1000  # 30 minutes, now expressed in milliseconds


def make_session(user_id, now):
    """Create a session for ``user_id`` starting at epoch ``now`` (ms)."""
    return {"user": user_id, "expires_at": now + SESSION_TTL_SECONDS}


def seconds_remaining(session, now):
    """Return time until ``session`` expires (negative once expired)."""
    return session["expires_at"] - now
