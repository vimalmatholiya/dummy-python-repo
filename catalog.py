"""Product catalog price lookups."""


def get_price(catalog, sku):
    """Return the unit price (a float, in dollars) for ``sku``."""
    return catalog[sku]
