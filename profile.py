"""User profile."""
from records import get_user_record


def profile_email(uid):
    """Return the email address from a user's record."""
    record = get_user_record(uid)
    return record[2]
