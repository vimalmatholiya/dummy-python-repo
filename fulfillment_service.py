"""Order fulfillment orchestration (in-diff caller)."""
from order_repo import get_order
from stock_service import available, reserve


def fulfill(store, inventory, order_id, warehouse):
    """Reserve stock for every line of ``order_id`` and return the reservation ids."""
    _oid, items, _address = get_order(store, order_id)
    reservations = []
    for line in items:
        if available(inventory, line["sku"]) >= line["qty"]:
            reservations.append(reserve(warehouse, line["sku"], line["qty"]))
    return reservations
