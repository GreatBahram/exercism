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
    return number * counter[number]


def full_house(counter):
    if len(counter) == 2 and counter.most_common()[0][1] == 3:
        return sum(key * value for key, value in counter.items())
    return 0


def four_of_a_kind(counter):
    most_common , count = counter.most_common()[0]
    if count >= 4:
        return most_common * 4
    return 0


def little_straight(counter):
    return 30 if sorted(counter.keys()) == [1, 2, 3, 4, 5] else 0


def big_straight(counter):
    return 30 if sorted(counter.keys()) == [2, 3, 4, 5, 6] else 0


def choice(counter):
    return sum(key * value for key, value in counter.items())


def yacht(counter):
    return 50 if len(counter) == 1 else 0


def score(dice, category):
    c = Counter(dice)
    function = {
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
    }.get(category)
    return function(c)
