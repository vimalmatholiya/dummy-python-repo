"""Signup form handling."""
from agevalidate import validate_age


def register(age):
    """Register a user, defaulting invalid ages to 0."""
    try:
        return validate_age(age)
    except (ValueError, TypeError):
        return 0
