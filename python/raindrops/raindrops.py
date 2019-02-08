from collections import namedtuple

Pair = namedtuple('Pair', ['factor', 'string'])

DROPS_LIST = [
    Pair(3, 'Pling'),
    Pair(5, 'Plang'),
    Pair(7, 'Plong'),
]


def raindrops(number: int) -> str:
    response = ''.join(
        pair.string
        for pair in DROPS_LIST
        if number % pair.factor == 0
    )
    return response or str(number)
