"""Stats dashboard."""
from stats import compute_stats


def render_mean(nums):
    """Render the mean of ``nums`` for the dashboard."""
    summary = compute_stats(nums)
    return f"mean={summary['mean']}"
