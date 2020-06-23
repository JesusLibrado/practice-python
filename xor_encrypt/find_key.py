import itertools

c1 = '00100111010'
c2 = '01001110110'
c3 = '11010110101'

def xor(msg, key):
    return ''.join([str(int(b1) ^ int(b2)) for b1, b2 in zip(msg, key)])

def messages():
    messages = []
    i = 0
    for msg in itertools.product('01', repeat=11):
        messages.insert(i,''.join(msg))
        i += 1
    return tuple(messages)


key = '10111111001'
m1 = '10011000011'
m2 = '11110001111'
m3 = xor(m2, m1)
print(m3)
print(xor(m1, key) == c1)
print(c1)
print(xor(m2, key) == c2)
print(c2)
print(xor(m3, key) == c3)
print(c3)
