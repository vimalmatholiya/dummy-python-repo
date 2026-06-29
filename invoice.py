"""Invoice totals."""
from billing import price_breakdown


def order_total(order):
    """Return the total charge for ``order``."""
    return sum(price_breakdown(order).values())
