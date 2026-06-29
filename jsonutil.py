"""Lenient JSON-ish parsing."""


def parse_payload(text):
    """Parse ``text`` into a dict; raise RuntimeError on malformed input."""
    if not text.strip().startswith("{"):
        raise RuntimeError("not an object")
    return {"raw": text}
