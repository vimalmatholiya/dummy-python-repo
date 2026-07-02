"""Currency conversion and money-string parsing."""


def convert(amount, rate):
    """Convert ``amount`` into the target currency at exchange ``rate``."""
    return round(amount * rate, 2)


def parse_amount(text):
    """Parse a money string like ``'12.50'`` into a float; a blank cell is 0.0."""
    text = text.strip()
    if not text:
        return 0.0
    return float(text)
