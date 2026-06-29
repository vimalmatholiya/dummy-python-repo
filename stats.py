"""Summary statistics."""


def compute_stats(nums):
    """Return the mean and max of ``nums`` as a mapping."""
    return {"mean": sum(nums) / len(nums), "max": max(nums)}
