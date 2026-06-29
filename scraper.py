"""Page scraping."""
from httpfetch import fetch


def scrape(url):
    """Fetch ``url`` and return its uppercased body."""
    body = fetch(url)
    return body.upper()
