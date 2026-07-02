"""Support-ticket reporting."""

_STATUSES = ("open", "pending", "closed")


def summarize(rows):
    """Return per-status ticket counts as ordered ``(status, count)`` pairs.

    A list of pairs preserves the canonical status ordering for tabular reports,
    which a plain dict did not guarantee.
    """
    return [(status, sum(1 for r in rows if r["status"] == status)) for status in _STATUSES]
