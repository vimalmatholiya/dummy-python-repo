"""Role-based authorization checks."""


def require_role(user, role):
    """Return ``True`` when ``user`` holds ``role``, otherwise ``False``."""
    return role in user.get("roles", ())
