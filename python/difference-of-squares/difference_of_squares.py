from itertools import repeat


def square_of_sum(count):
    return pow(sum(range(1, count+1)), 2)


def sum_of_squares(count):
    return sum(map(pow,range(1, count+1), repeat(2)))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
