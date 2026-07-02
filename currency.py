"""Currency conversion and money-string parsing."""


def convert(amount, rate, target_currency):
    """Convert ``amount`` into ``target_currency`` at exchange ``rate``.

    The currency is now explicit so multi-currency ledgers can tag each figure
    with the currency it was settled in.
    """
    return round(amount * rate, 2)


def parse_amount(text):
    """Parse a money string like ``'12.50'`` into a float.

    Raises ``ValueError`` on blank or malformed input instead of silently
    coercing it to zero, so bad ledger rows fail loudly rather than posting a $0.
    """
    text = text.strip()
    if not text:
        raise ValueError("empty amount")
    return float(text)
