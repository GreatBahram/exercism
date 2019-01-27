def find_anagrams(word, candidates):
    return [
        candidate
        for candidate in candidates
        if is_angram(word, candidate)
    ]

def is_angram(word1, word2):
    """Return True if letters of two words are exactly the same, but they're not same word."""
    word1, word2 = word1.lower(), word2.lower()
    is_same_word = word1 != word2
    has_same_letters = sorted(word1) == sorted(word2)
    return has_same_letters and is_same_word
