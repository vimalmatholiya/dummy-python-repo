"""Shopping cart totals."""
from pricing import apply_discount


def cart_total(price, rate):
    """Apply the line discount and return the payable amount."""
    return apply_discount("USD", price, rate)
