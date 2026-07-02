"""Order persistence."""


def get_order(store, order_id):
    """Return the order record for ``order_id`` as a dict."""
    return store[order_id]
