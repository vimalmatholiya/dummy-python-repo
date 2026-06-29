"""A tiny in-memory account ledger (scenario 4: exception contract)."""


def withdraw(balance, amount):
    """Withdraw ``amount`` from ``balance``; raise ValueError on overdraft."""
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
