"""Tiny SQL string builder."""


def build_query(table, where, order_by, limit):
    """Build a SELECT statement for ``table``."""
    return f"SELECT * FROM {table} WHERE {where} ORDER BY {order_by} LIMIT {limit}"
