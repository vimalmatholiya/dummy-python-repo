"""HTTP fetching (stub)."""


def fetch(url):
    """Return the body for ``url``; raise ConnectionError when ``url`` is empty."""
    if not url:
        raise ConnectionError("empty url")
    return f"body:{url}"
