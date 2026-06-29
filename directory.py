"""Employee directory."""
from namefmt import format_name


def display_name(first, last):
    """Return the directory display name for an employee."""
    return format_name(first, "", last)
