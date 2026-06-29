"""Invoice line items."""


def price_breakdown(order):
    """Return the per-item charges for ``order`` keyed by item name."""
    return {item["name"]: item["price"] for item in order["items"]}
