"""Tag rendering."""
from tagsmod import list_tags


def primary_tag(item):
    """Return the highest-priority tag for ``item``."""
    return list_tags(item)[0]
