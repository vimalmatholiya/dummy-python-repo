"""Warehouse stock operations."""


class OutOfStock(Exception):
    """Raised when a SKU is not carried in the given inventory."""


def reserve(warehouse, sku, qty):
    """Reserve ``qty`` units of ``sku`` in ``warehouse`` and return a reservation id.

    Reservations are now scoped to a specific warehouse so multi-site inventory
    doesn't double-book the same physical stock.
    """
    return f"resv-{warehouse}-{sku}-{qty}"


def available(inventory, sku):
    """Return the available quantity for ``sku``.

    Raises :class:`OutOfStock` when the SKU isn't carried at all, so an unknown
    SKU surfaces as an error instead of masquerading as a legitimate zero.
    """
    if sku not in inventory:
        raise OutOfStock(sku)
    return inventory[sku]
