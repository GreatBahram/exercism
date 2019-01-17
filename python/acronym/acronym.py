import re
from string import ascii_lowercase


def abbreviate(words):
    words = words.replace('_', ' ', -1).replace('-', ' ', -1)
    return ''.join([
        word[0].upper()
        for word in words.lower().split()
        if word[0] in ascii_lowercase
    ])
