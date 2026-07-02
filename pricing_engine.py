"""Order pricing: turns line items into a payable total."""
from money import apply_tax


def line_subtotal(line):
    """Return ``qty * unit_price`` for one order ``line``."""
    return line["qty"] * line["unit_price"]


def compute_total(lines, tax_rate, discount):
    """Return the tax-inclusive total for ``lines`` after applying ``discount``.

    ``discount`` is a fraction (e.g. 0.10 for 10% off) applied to the subtotal
    before tax is added.
    """
    subtotal = sum(line_subtotal(line) for line in lines)
    subtotal -= subtotal * discount
    return apply_tax(subtotal, tax_rate)
