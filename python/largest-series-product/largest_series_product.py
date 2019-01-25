def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def sections(series, size):
    """return all sections of series."""
    return(
        series[i: i+size]
        for i in range(len(series)-size+1)
    )

def largest_product(series, size):
    if size < 0:
        raise ValueError('Bad size!')
    digits = [int(n) for n in series]
    return max(
        product(numbers)
        for numbers in sections(digits, size)
    )
