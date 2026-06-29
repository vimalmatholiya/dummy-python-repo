"""Settings access."""
from config_reader import parse_config


def get_value(text, key):
    """Return the configured value for ``key``."""
    return dict(parse_config(text))[key]
