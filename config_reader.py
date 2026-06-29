"""Minimal config reader."""


def parse_config(text):
    """Parse ``key=value`` lines into a list of (key, value) pairs."""
    return [tuple(line.split("=")) for line in text.splitlines()]
