import itertools

def vigenere_encrypt(plaintext, codeword):
    plaintext = plaintext.upper()
    codeword = codeword.upper()
    encrypted = ''
    for text, code in zip(plaintext, itertools.cycle(codeword)):
        diff = ord(code)-ord('A')
        letter = ord(text) + diff
        if letter > ord('Z'):
            outbound = letter-ord('Z')-1
            encrypted += chr(ord('A')+outbound)
        else:
            encrypted += chr(letter)
    return encrypted

text = "attackatdawn"
code = "lemon"

print(vigenere_encrypt(text, code))