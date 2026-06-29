"""Token minting."""


def make_token(user_id, ttl):
    """Build a session token for ``user_id`` lasting ``ttl`` seconds."""
    return f"{user_id}:{ttl}"
