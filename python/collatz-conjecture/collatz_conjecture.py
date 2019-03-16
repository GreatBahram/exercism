def collatz_steps(number):
    """Return steps required to reach to 1."""
    if number <= 0:
        raise ValueError('Number should be positive.')

    steps = 0
    while number > 1:
        if is_even(number):
            number = number / 2
        else:
            number = 3 * number + 1
        steps += 1
    return steps


def is_even(number):
    """return True if number is even."""
    return number % 2 == 0
