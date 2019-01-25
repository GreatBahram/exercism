from functools import reduce


def get_product(series, size):
    """return a product each time."""
    if size == len(series):
        yield series
    else:
        index = 0
        while True:
            item = series[index: index+size]
            if len(item) == size:
                yield item
                index += 1
            else:
                break

def largest_product(series, size):
    series = [int(n) for n in series]
    if size > len(series):
        raise ValueError('Bad size!')
    if size == 0:
        return 1

    return max(
        reduce(lambda x, y: x * y , product)
        for product in get_product(series, size)
    )
