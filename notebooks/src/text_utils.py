"""Utilities for cleaning text."""


def clean_name(raw):
    """Clean and format a name."""
    # TODO: collapse whitespace, then title-case
    clean = " ".join(raw.split())
    return clean.title()
