"""Content tagging."""


def list_tags(item):
    """Return ``item``'s tags as a set (deduplicated)."""
    return {t for t in item["tags"]}
