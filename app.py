import re

def slugify(raw_text: str) -> str:
    """
    Convert *source_text* into a lowercase dash-separated slug.
    Keeps alphanumerics, converts spaces & punctuation to '-',
    collapses consecutive dashes.
    """
    source_text = source_text.lower()
    source_text = re.sub(r"[^a-z0-9]+", "-", source_text)
    return re.sub(r"-{2,}", "-", source_text).strip("-")