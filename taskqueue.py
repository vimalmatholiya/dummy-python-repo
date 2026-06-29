"""In-memory task queue."""


def pop_task(queue):
    """Remove and return the next task, or None when empty."""
    if not queue:
        return None
    return queue.pop(0)
