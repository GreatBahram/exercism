from math import floor, sqrt


def prime_factors(natural_number):
    if natural_number == 1:
        return set()
    for n in range(2, floor(sqrt(natural_number) + 1)):
        if natural_number % n == 0:
            return [n, *prime_factors(natural_number//n)]

