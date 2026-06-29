"""Age validation."""


def validate_age(age):
    """Return ``age`` if valid, else raise TypeError."""
    if age < 0:
        raise TypeError("age must be non-negative")
    return age
