 # initializing string 
str = input("Input: ")


def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r

print(simple_hash(str))