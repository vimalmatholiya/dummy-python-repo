"""Order fulfillment orchestration (in-diff caller)."""
from order_repo import get_order
from stock_service import available, reserve


def fulfill(store, inventory, order_id):
    """Reserve stock for every line of ``order_id`` and return the reservation ids."""
    order = get_order(store, order_id)
    reservations = []
    for line in order["items"]:
        if available(inventory, line["sku"]) >= line["qty"]:
            reservations.append(reserve(line["sku"], line["qty"]))
    return reservations
