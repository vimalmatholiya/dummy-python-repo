"""Look up users by id (scenario 5: exception contract)."""


def find_user(users, uid):
    """Return the user with ``uid``; raise KeyError if there is none."""
    for user in users:
        if user["id"] == uid:
            return user
    raise KeyError(uid)
