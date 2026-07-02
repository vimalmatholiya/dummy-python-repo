"""Bank statement ingestion (out-of-diff caller of currency.parse_amount)."""
from currency import parse_amount


def total_deposits(rows):
    """Sum the deposit column across statement ``rows`` (blank cells count as zero)."""
    return sum(parse_amount(row["deposit"]) for row in rows)
