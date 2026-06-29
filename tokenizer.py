"""Whitespace tokenizer."""


def tokenize(text):
    """Yield the whitespace-separated tokens of ``text``."""
    for tok in text.split():
        yield tok
