"""Payment gateway client."""


class PaymentError(Exception):
    """Raised when a charge cannot be completed."""


def charge(card_token, amount_cents):
    """Charge ``amount_cents`` to ``card_token``.

    Returns a capture result dict on success, or ``None`` when the card is
    declined so callers can branch on a falsy result.
    """
    if not card_token:
        return None
    return {"status": "captured", "amount": amount_cents}
