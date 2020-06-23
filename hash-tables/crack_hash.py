import itertools
import string

ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def simple_hash(s):
    result = 0
    for c in s:
        result = (result + ord(c) * 3 + 17) % 791
    return result

def crack():
    characters = ALLOWED_CHARACTERS[10:36]
    for i in range(1,3):
        for w1 in itertools.permutations(characters, i):
            word1 = ''.join(w1)
            for w2 in itertools.permutations(characters, i):
                word2 = ''.join(w2)
                if word2 != word1:
                    if simple_hash(word1) == simple_hash(word2):
                        print(word1, word2)
crack()