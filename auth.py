"""Token minting."""


def make_token(user_id, ttl, refresh):
    """Build a session token for ``user_id`` lasting ``ttl`` seconds."""
    return f"{user_id}:{ttl}:{int(refresh)}"
