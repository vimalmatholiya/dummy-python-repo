"""Order state transitions."""

VALID_STATES = ("pending", "captured", "shipped")


def mark_paid(order):
    """Advance ``order`` into the captured state after a successful charge."""
    order["status"] = "captured"
    return order
