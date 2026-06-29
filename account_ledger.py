"""A tiny in-memory account ledger (scenario 4: exception contract)."""


def withdraw(balance, amount):
    """Withdraw ``amount`` from ``balance`` and return the new balance."""
    return balance - amount
