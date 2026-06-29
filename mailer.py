"""Outbound email."""


def send_email(to, subject, body):
    """Queue an email to ``to`` and return a status string."""
    return f"queued:{to}:{subject}"
