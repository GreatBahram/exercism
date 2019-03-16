DROPS_DICT = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
}


def raindrops(number: int) -> str:
    response = ''.join(
        string
        for factor, string in DROPS_DICT.items()
        if number % factor == 0
    )
    return response or str(number)
