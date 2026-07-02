"""Order persistence."""


def get_order(store, order_id):
    """Return the order for ``order_id`` as an ``(order_id, items, address)`` triple.

    Returning a tuple stops callers from mutating the stored order in place.
    """
    record = store[order_id]
    return (order_id, record["items"], record["address"])
