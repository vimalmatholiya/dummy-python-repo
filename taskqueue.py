"""In-memory task queue."""


def pop_task(queue):
    """Remove and return the next task; raise IndexError when empty."""
    if not queue:
        raise IndexError("empty queue")
    return queue.pop(0)
