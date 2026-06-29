"""List pagination."""


def paginate(items, page, size):
    """Return the ``page``-th slice of ``items`` (``size`` per page)."""
    start = page * size
    return items[start:start + size]
