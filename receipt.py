"""Customer-facing receipt rendering."""
from pricing_engine import compute_total
from money import format_money


def render_receipt(order):
    """Return a printable receipt summary line for ``order``."""
    total = compute_total(order["lines"], order["tax_rate"])
    return f"Total due: {format_money(total)}"
