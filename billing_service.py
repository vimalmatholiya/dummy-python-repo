"""Billing: renders an order total in the customer's currency (in-diff caller)."""
from currency import convert
from fx_rates import get_rate


def bill_in_currency(total_usd, target_currency):
    """Return ``total_usd`` billed in ``target_currency``."""
    rate = get_rate("USD", target_currency)
    return convert(total_usd, rate)
