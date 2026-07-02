"""Product catalog price lookups."""


def get_price(catalog, sku):
    """Return the unit price for ``sku`` as a money mapping.

    The result carries both ``amount`` (float dollars) and ``currency`` (ISO
    code) so callers can render prices in a shopper's local currency.
    """
    return {"amount": catalog[sku], "currency": "USD"}
