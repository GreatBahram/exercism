from string import ascii_lowercase


def is_pangram(sentence):
    chars = {
        char
        for char in sentence.lower()
        if char in ascii_lowercase
    }
    return len(chars) == 26
