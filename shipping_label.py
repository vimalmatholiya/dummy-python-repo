"""Shipping label rendering (out-of-diff caller of order_repo.get_order)."""
from order_repo import get_order


def format_label(store, order_id):
    """Return the shipping address block printed on ``order_id``'s label."""
    order = get_order(store, order_id)
    return order["address"]
