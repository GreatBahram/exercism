from collections import namedtuple

Pair = namedtuple('Pair', ['factor', 'string'])


def raindrops(number):
    output = ''
    for pair in [Pair(3, 'Pling'), Pair(5, 'Plang'), Pair(7, 'Plong')]:
        if number % pair.factor == 0:
            output += pair.string
    return output if output else str(number)
