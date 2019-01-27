import re

ISBN_RE = re.compile(r"""
    ^
    \d
    \D*
    \d{3}
    \D*
    \d{5}
    \D*
    (\d|X)$
""", re.VERBOSE)


def verify(isbn):
    if not is_valid_isbn(isbn):
        return False

    numbers = [
        10 if char == 'X' else int(char)
        for char in isbn
        if char != '-'
    ]

    return sum(
        index * int(number)
        for index, number in enumerate(numbers[::-1], 1) 
    ) % 11 == 0


def is_valid_isbn(isbn):
    """Return True if isbn style matches."""
    return bool(ISBN_RE.search(isbn))
