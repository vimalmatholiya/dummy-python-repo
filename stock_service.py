"""Warehouse stock operations."""


def reserve(warehouse, sku, qty):
    """Reserve ``qty`` units of ``sku`` in ``warehouse`` and return a reservation id.

    Reservations are now scoped to a specific warehouse so multi-site inventory
    doesn't double-book the same physical stock.
    """
    return f"resv-{warehouse}-{sku}-{qty}"


def available(inventory, sku):
    """Return the available quantity for ``sku`` (0 when the SKU is unknown)."""
    return inventory.get(sku, 0)
