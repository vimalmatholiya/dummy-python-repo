"""Support dashboard badge (out-of-diff caller of report_service.summarize)."""
from report_service import summarize


def open_ticket_count(rows):
    """Return how many tickets are currently open, for the dashboard badge."""
    return summarize(rows)["open"]
