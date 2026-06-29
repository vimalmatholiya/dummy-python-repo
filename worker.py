"""Task worker loop."""
from taskqueue import pop_task


def drain(queue):
    """Process every queued task and return how many ran."""
    count = 0
    while True:
        task = pop_task(queue)
        if task is None:
            break
        count += 1
    return count
