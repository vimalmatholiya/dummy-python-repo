"""Activity feed."""
from pagination import paginate


def first_page(items):
    """Return the first page of ``items`` using the default page size."""
    return paginate(items, 0)
