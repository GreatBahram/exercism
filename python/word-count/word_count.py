import re
from collections import Counter

WORD_RE = re.compile(r"[^\s\n\t_,.,:&!@$%\^]+")


def word_count(phrase):
    return Counter(map(normalize, WORD_RE.findall(phrase)))
    

def normalize(word):
    if word.startswith("'"):
        word = word[1:-1]
    return word.lower()
