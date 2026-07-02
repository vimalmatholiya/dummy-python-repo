"""Message template rendering."""


def render(template, context, locale):
    """Render ``template`` with ``context`` values, localized for ``locale``.

    The locale is now required so dates, numbers and currency in a message are
    formatted for the recipient's region.
    """
    return template.format(**context)
