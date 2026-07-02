"""Background job that purges expired sessions."""
from session_store import SESSION_TTL_SECONDS


def purge_cutoff(now):
    """Return the epoch-second cutoff before which sessions are purgeable."""
    return now - SESSION_TTL_SECONDS
