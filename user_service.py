"""Service layer that resolves users for a request (scenario 5 caller)."""
from user_lookup import find_user


def describe_user(users, uid):
    """Return a label for ``uid``, falling back to "guest" when lookup fails."""
    user = find_user(users, uid)
    if user is None:
        return "guest"
    return user["name"]
