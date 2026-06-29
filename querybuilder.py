"""Tiny SQL string builder."""


def build_query(table, where, limit):
    """Build a SELECT statement for ``table``."""
    return f"SELECT * FROM {table} WHERE {where} LIMIT {limit}"
