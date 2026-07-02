"""Invoice CSV export (out-of-diff caller of fx_rates.get_rate)."""
from fx_rates import get_rate


def line_in_eur(amount_usd):
    """Return ``amount_usd`` expressed in EUR for the exported invoice line."""
    return amount_usd * get_rate("USD", "EUR")
