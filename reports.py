"""Report queries."""
from querybuilder import build_query


def recent_orders(limit):
    """Build the query for the most recent orders."""
    return build_query("orders", "paid = 1", limit)
