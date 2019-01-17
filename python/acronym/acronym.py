import re


def abbreviate(words):
    ACRONYM_RE = re.compile(r'\b[-_]?([a-zA-Z])')
    return ''.join(map(lambda c: c.upper(), ACRONYM_RE.findall(words.replace("'", ''))))
