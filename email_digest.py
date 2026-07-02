"""Daily email digest (in-diff caller of render + summarize)."""
from report_service import summarize
from template_engine import render


def build_digest(rows, template, locale="en_US"):
    """Render the daily ticket digest email body."""
    counts = dict(summarize(rows))
    return render(template, {"open": counts["open"], "closed": counts["closed"]}, locale)
