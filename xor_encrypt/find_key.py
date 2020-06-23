c1 = tuple('00100111010')
c2 = tuple('01001110110')
c3 = tuple('11010110101')

def xor(msg, key):
    return ''.join([str(int(b1) ^ int(b2)) for b1, b2 in zip(msg, key)])

