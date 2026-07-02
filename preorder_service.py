"""Pre-order holds (out-of-diff caller of stock_service.reserve)."""
from stock_service import reserve


def hold_preorder(sku, qty):
    """Place a reservation hold for a pre-ordered item."""
    return reserve(sku, qty)
