from itertools import combinations_with_replacement
from string import ascii_uppercase, digits


def random_name():
    numbers = combinations_with_replacement(digits * 3, 3)
    words = combinations_with_replacement(ascii_uppercase * 2, 2)
    while True:
        name = '{}{}{}{}{}'.format(*next(words), *next(numbers))
        yield name

names = random_name()


class Robot:
    def __init__(self):
        self.name = next(names)

    def reset(self):
        self.name = next(names)
