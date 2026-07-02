"""Shopping-cart total computation."""
from catalog import get_price


def cart_total(catalog, cart):
    """Return the total dollar cost of ``cart`` (a list of {sku, qty})."""
    total = 0.0
    for item in cart:
        total += item["qty"] * get_price(catalog, item["sku"])
    return total
