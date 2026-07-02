"""Session lifecycle helpers (all times in epoch seconds)."""

SESSION_TTL_SECONDS = 1800  # 30 minutes


def make_session(user_id, now):
    """Create a session for ``user_id`` starting at epoch-second ``now``."""
    return {"user": user_id, "expires_at": now + SESSION_TTL_SECONDS}


def seconds_remaining(session, now):
    """Return seconds until ``session`` expires (negative once expired)."""
    return session["expires_at"] - now
