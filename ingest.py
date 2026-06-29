"""Payload ingestion."""
from jsonutil import parse_payload


def ingest(text):
    """Parse a payload, returning None when it is malformed."""
    try:
        return parse_payload(text)
    except ValueError:
        return None
