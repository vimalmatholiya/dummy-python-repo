"""Checkout orchestration: price the order and capture payment."""
from pricing_engine import compute_total
from payments_gateway import charge
from money import to_cents


def checkout(order, card_token):
    """Price ``order``, charge ``card_token``, and return a confirmation dict."""
    total = compute_total(order["lines"], order["tax_rate"], order.get("discount", 0.0))
    result = charge(card_token, to_cents(total))
    if result is None:
        return {"ok": False, "reason": "card_declined"}
    return {"ok": True, "charged_cents": result["amount"]}
