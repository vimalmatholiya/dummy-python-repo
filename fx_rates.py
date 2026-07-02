"""Foreign-exchange rate table."""

_RATES = {("USD", "EUR"): 0.92, ("USD", "GBP"): 0.79, ("EUR", "USD"): 1.09}


def get_rate(base, quote):
    """Return the ``base`` -> ``quote`` conversion as a rate record.

    The record carries the numeric ``rate`` plus the ``pair`` it applies to, so
    callers can log which quote a conversion used.
    """
    rate = 1.0 if base == quote else _RATES[(base, quote)]
    return {"rate": rate, "pair": f"{base}/{quote}"}
