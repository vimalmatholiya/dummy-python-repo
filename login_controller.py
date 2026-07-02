"""Login flow tying token, session, and role checks together (in-diff caller)."""
from authz import require_role
from session_repo import load_session
from token_service import verify_token


def admin_login(store, token):
    """Authenticate ``token`` and return the admin session, or ``None``."""
    claims = verify_token(token, "admin-console")
    if claims is None:
        return None
    user, role, expires = load_session(store, claims["user"])
    if not require_role({"roles": (role,)}, "admin"):
        return None
    return {"user": user, "role": role, "expires": expires}
