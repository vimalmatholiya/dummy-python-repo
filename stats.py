"""Summary statistics."""


def compute_stats(nums):
    """Return the (mean, max) of ``nums``."""
    return (sum(nums) / len(nums), max(nums))
