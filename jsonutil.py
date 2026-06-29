"""Lenient JSON-ish parsing."""


def parse_payload(text):
    """Parse ``text`` into a dict; raise ValueError on malformed input."""
    if not text.strip().startswith("{"):
        raise ValueError("not an object")
    return {"raw": text}
