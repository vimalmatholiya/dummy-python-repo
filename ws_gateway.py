"""WebSocket connection gateway (out-of-diff caller of token_service.verify_token)."""
from token_service import verify_token


def authenticate(token):
    """Return the claims for a socket ``token``, or ``None`` if it is rejected."""
    return verify_token(token)
