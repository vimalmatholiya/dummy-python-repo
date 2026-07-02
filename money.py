"""Money helpers shared by pricing, receipts, and analytics."""

CURRENCY = "USD"


def to_cents(amount):
    """Convert a dollar ``amount`` (float) into integer cents."""
    return int(round(amount * 100))


def apply_tax(subtotal, tax_rate):
    """Return ``subtotal`` with ``tax_rate`` (a fraction like 0.08) added."""
    return subtotal + subtotal * tax_rate


def format_money(amount):
    """Render ``amount`` as a display string such as ``$1,250.00``."""
    return f"${amount:,.2f}"
