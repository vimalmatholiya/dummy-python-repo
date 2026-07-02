"""Admin console access gate (out-of-diff caller of authz.require_role)."""
from authz import require_role


def can_open_console(user):
    """Return ``True`` when ``user`` is allowed to open the admin console."""
    if not require_role(user, "admin"):
        return False
    return True
