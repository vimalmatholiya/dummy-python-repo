"""Foreign-exchange rate table."""

_RATES = {("USD", "EUR"): 0.92, ("USD", "GBP"): 0.79, ("EUR", "USD"): 1.09}


def get_rate(base, quote):
    """Return the conversion rate from ``base`` currency to ``quote`` currency."""
    if base == quote:
        return 1.0
    return _RATES[(base, quote)]
