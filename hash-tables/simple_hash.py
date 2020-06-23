 # initializing string 
str = input("Input: ")

def simple_hash1(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r

print(simple_hash1(str))

def simple_hash2(s):
    result = 0
    for c in s:
        result = (result + ord(c) * 3 + 17) % 791
    return result

print(simple_hash2(str))