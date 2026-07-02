"""Support-ticket reporting."""

_STATUSES = ("open", "pending", "closed")


def summarize(rows):
    """Return per-status ticket counts as a ``{status: count}`` mapping."""
    return {status: sum(1 for r in rows if r["status"] == status) for status in _STATUSES}
