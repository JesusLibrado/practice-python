def encrypt(plaintext, k): 
    if(len(plaintext)!=len(k)):
        return

    return repr(''.join([chr(ord(t_byte)^ord(k_byte)) for t_byte, k_byte in zip(plaintext, k)]))

input_text = "hello"
k = "world"

print(encrypt(input_text, k))