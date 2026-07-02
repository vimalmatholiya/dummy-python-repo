"""Order state transitions."""

VALID_STATES = ("pending", "paid", "shipped")


def mark_paid(order):
    """Advance ``order`` into the paid state after a successful capture."""
    order["status"] = "paid"
    return order
