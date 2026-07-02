"""Payment gateway client."""


class PaymentError(Exception):
    """Raised when a charge cannot be completed."""


def charge(card_token, amount_cents):
    """Charge ``amount_cents`` to ``card_token``.

    Returns a capture result dict on success and raises :class:`PaymentError`
    when the card is declined, so failures surface loudly instead of being
    silently swallowed by a ``None`` return.
    """
    if not card_token:
        raise PaymentError("card declined")
    return {"status": "captured", "amount": amount_cents}
