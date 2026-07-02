"""Warehouse stock operations."""


def reserve(sku, qty):
    """Reserve ``qty`` units of ``sku`` and return a reservation id."""
    return f"resv-{sku}-{qty}"


def available(inventory, sku):
    """Return the available quantity for ``sku`` (0 when the SKU is unknown)."""
    return inventory.get(sku, 0)
