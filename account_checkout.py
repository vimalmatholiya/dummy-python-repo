"""Checkout flow that debits an account (scenario 4 caller)."""
from account_ledger import withdraw


def checkout(balance, price):
    """Debit ``price`` from ``balance`` and return the remaining funds, or None."""
    if price > balance:
        return None
    remaining = withdraw(balance, price)
    return remaining
