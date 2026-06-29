"""Minimal config reader."""


def parse_config(text):
    """Parse ``key=value`` lines into a mapping."""
    return {k: v for k, v in (line.split("=") for line in text.splitlines())}
