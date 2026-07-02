"""Message template rendering."""


def render(template, context):
    """Render ``template`` by substituting ``context`` values into it."""
    return template.format(**context)
