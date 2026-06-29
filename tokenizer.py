"""Whitespace tokenizer."""


def tokenize(text):
    """Return the whitespace-separated tokens of ``text`` as a list."""
    return [tok for tok in text.split()]
