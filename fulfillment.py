"""Warehouse fulfillment gating."""


def can_ship(order):
    """Return True when ``order`` is paid and may be handed to the warehouse."""
    return order.get("status") == "paid"
