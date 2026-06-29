"""Order pricing helpers."""


def apply_discount(currency, price, rate):
    """Return ``price`` (in ``currency``) reduced by ``rate``."""
    return price * (1 - rate)
