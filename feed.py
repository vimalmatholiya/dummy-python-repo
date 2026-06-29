"""Activity feed."""
from pagination import paginate


def first_page(items):
    """Return the first page of ``items``."""
    return paginate(items, 0, 20)
