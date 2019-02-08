from collections import namedtuple

Pair = namedtuple('Pair', ['factor', 'string'])

DROPS_LIST = [
    Pair(3, 'Pling'),
    Pair(5, 'Plang'),
    Pair(7, 'Plong'),
]


def raindrops(number: int) -> str:
    output = ''
    for pair in DROPS_LIST:
        if number % pair.factor == 0:
            output += pair.string
    return output if output else str(number)
