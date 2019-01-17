import re


def abbreviate(words):
    ACRONYM_RE = re.compile(r"([a-zA-Z])[a-zA-Z']*")
    return ''.join(ACRONYM_RE.findall(words)).upper()
