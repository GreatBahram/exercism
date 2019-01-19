from collections import Counter
from functools import partial

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def first_sixth(number, counter):
    print(counter.items())
    return number * len([value for key, value in counter.items() if key == number])

def full_house(counter):
    return sum([key * value for key, value in counter.items()])

def four_of_a_kind(counter):
    return sum([key * value for key, value in counter.items() if key == 4])

def little_straight():
    return 30

def big_straight():
    return 30

def choice(counter):
    return sum([key * value for key, value in counter.items()])

def yacht(counter):
    return 50 if len(counter) == 1 else 0


def score(dice, category):
    c = Counter(dice)
    options = {
        YACHT : yacht,
        ONES : partial(first_sixth, 1),
        TWOS : partial(first_sixth, 2),
        THREES : partial(first_sixth, 3),
        FOURS : partial(first_sixth, 4),
        FIVES : partial(first_sixth, 5),
        SIXES : partial(first_sixth, 6),
        FULL_HOUSE : full_house,
        FOUR_OF_A_KIND : four_of_a_kind,
        LITTLE_STRAIGHT : little_straight,
        BIG_STRAIGHT : big_straight,
        CHOICE : choice,
    }.get(category)(c)
