"""Order pricing helpers."""


def apply_discount(price, rate):
    """Return ``price`` reduced by ``rate`` (a 0..1 fraction)."""
    return price * (1 - rate)
