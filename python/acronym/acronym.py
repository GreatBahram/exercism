import re


def abbreviate(words):
    ACRONYM_RE = re.compile(r"\b[-_]?([a-zA-Z])[a-zA-Z']*")
    return ''.join(ACRONYM_RE.findall(words)).upper()
