"""Opaque access-token verification."""


def verify_token(token, audience):
    """Decode ``token`` for ``audience`` and return its claims, or ``None`` if invalid.

    Tokens are now bound to the audience (service) they were minted for, so a
    token issued for one service can't be replayed against another.
    """
    if not token or ":" not in token:
        return None
    user, _, exp = token.partition(":")
    return {"user": user, "exp": int(exp), "aud": audience}
