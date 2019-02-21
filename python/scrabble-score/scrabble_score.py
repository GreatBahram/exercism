scramble_scores = [
    (1, 'A E I O U L N R S T'),
    (2, 'D G'),
    (3, 'B C M P'),
    (4, 'F H V W Y'),
    (5, 'K'),
    (8, 'J X'),
    (10, 'Q Z'),
]

LETTER_SCORES = {
    letter: key
    for key, letters in scramble_scores
    for letter in letters.split()
}


def score(word):
    return sum(
        LETTER_SCORES.get(char.upper(), 0)
        for char in word
    )
