"""User notifications."""
from mailer import send_email


def notify(address, message):
    """Send a welcome email to ``address``."""
    return send_email(address, "Welcome", message)
