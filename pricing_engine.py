"""Order pricing: turns line items into a payable total."""
from money import apply_tax


def line_subtotal(line):
    """Return ``qty * unit_price`` for one order ``line``."""
    return line["qty"] * line["unit_price"]


def compute_total(lines, tax_rate):
    """Return the tax-inclusive total for a list of order ``lines``."""
    subtotal = sum(line_subtotal(line) for line in lines)
    return apply_tax(subtotal, tax_rate)
