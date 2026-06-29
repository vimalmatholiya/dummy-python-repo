"""Age validation."""


def validate_age(age):
    """Return ``age`` if valid, else raise ValueError."""
    if age < 0:
        raise ValueError("age must be non-negative")
    return age
