"""Word counting."""
from tokenizer import tokenize


def word_count(text):
    """Return the number of tokens in ``text``."""
    return len(tokenize(text))
