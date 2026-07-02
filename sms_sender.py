"""Transactional SMS delivery (out-of-diff caller of template_engine.render)."""
from template_engine import render


def send_sms(phone, template, context):
    """Format and enqueue a transactional SMS to ``phone``."""
    body = render(template, context)
    return {"to": phone, "body": body}
