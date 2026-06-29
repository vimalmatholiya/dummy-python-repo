"""Entry point that loads settings strictly (scenario 2 caller)."""
from settings_loader import load_settings


def bootstrap(config_path):
    """Load configuration, failing fast on a missing required name."""
    settings = load_settings(config_path, strict=True)
    return settings["name"]
