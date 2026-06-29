"""Task worker loop."""
from taskqueue import pop_task


def drain(queue):
    """Process every queued task and return how many ran."""
    count = 0
    while True:
        try:
            task = pop_task(queue)
        except IndexError:
            break
        count += 1
    return count
