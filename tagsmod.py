"""Content tagging."""


def list_tags(item):
    """Return ``item``'s tags as a list (priority order preserved)."""
    return [t for t in item["tags"]]
