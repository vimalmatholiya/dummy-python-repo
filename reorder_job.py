"""Nightly reorder job (out-of-diff caller of stock_service.available)."""
from stock_service import available


def needs_reorder(inventory, sku, threshold):
    """Return ``True`` when the stock level for ``sku`` has fallen below ``threshold``."""
    return available(inventory, sku) < threshold
