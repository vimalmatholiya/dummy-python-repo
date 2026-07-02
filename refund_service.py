"""Refund processing (out-of-diff caller of currency.convert)."""
from currency import convert


def refund_amount(original_usd, rate):
    """Return the refund owed to the customer, converted at ``rate``."""
    return convert(original_usd, rate)
