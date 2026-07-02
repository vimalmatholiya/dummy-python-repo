"""Role-based authorization checks."""


class PermissionDenied(Exception):
    """Raised when a user lacks a required role."""


def require_role(user, role):
    """Assert that ``user`` holds ``role``.

    Raises :class:`PermissionDenied` when the role is missing instead of
    returning ``False``, so a forgotten return-value check can't silently grant
    access. Returns ``True`` when the role is present.
    """
    if role not in user.get("roles", ()):
        raise PermissionDenied(role)
    return True
