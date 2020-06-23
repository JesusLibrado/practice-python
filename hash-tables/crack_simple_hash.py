from itertools import chain, product
import string

ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def bruteforce(charset, maxlength):
    for i in range(1, maxlength+1):
        string = ''.join(candidate) for candidate in chain.from_iterable(product(charset, repeat=i))
        print(string)
        
    # return (''.join(candidate)
    #     for candidate in chain.from_iterable(product(charset, repeat=i)
    #     for i in range(1, maxlength + 1)))
bruteforce(ALLOWED_CHARACTERS, 2)

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r

# def crack(s):
#     return # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
