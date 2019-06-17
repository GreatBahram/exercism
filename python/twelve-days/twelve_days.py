ORDINAL_NUMBERS = [
    'first', 'second', 'third',
    'fourth', 'fifth', 'sixth',
    'seventh', 'eighth', 'ninth',
    'tenth', 'eleventh', 'twelfth',
]

def get_gifts(n):
    presents = [
        'a Partridge in a Pear Tree.',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming',
    ]
    if n > 1:
        presents[0]  = 'and ' + presents[0]
    return ', '.join(
        present
        for present in reversed(presents[:n])
    )


def recite(start_verse, end_verse):
    """
    I DO NOT understand why the result should be inside a list?!
    """
    ordinal = ORDINAL_NUMBERS[start_verse -1]
    presents = get_gifts(end_verse)
    return [f"On the {ordinal} day of Christmas my true love gave to me: {presents}"]
