"""Tag rendering."""
from tagsmod import list_tags


def primary_tag(item):
    """Return any tag for ``item``."""
    return next(iter(list_tags(item)))
