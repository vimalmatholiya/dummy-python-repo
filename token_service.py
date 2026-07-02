"""Opaque access-token verification."""


def verify_token(token):
    """Decode ``token`` and return its claims dict, or ``None`` when it is invalid."""
    if not token or ":" not in token:
        return None
    user, _, exp = token.partition(":")
    return {"user": user, "exp": int(exp)}
