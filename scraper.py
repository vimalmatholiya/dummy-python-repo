"""Page scraping."""
from httpfetch import fetch


def scrape(url):
    """Fetch ``url`` and return its uppercased body."""
    try:
        body = fetch(url)
    except ConnectionError:
        return ""
    return body.upper()
