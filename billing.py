"""Invoice line items."""


def price_breakdown(order):
    """Return the per-item charges for ``order`` as a list."""
    return [item["price"] for item in order["items"]]
