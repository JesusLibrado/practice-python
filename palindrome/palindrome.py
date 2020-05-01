word = input("Enter word: ")

def isPalindrome(input_string):
    input_length = len(input_string)
    if input_length == 1: return True
    half_index = input_length//2
    first_half = input_string[0:half_index] 
    second_half = input_string[half_index:input_length] if input_length % 2 == 0 else input_string[half_index+1:input_length]
    reverse_string = first_half [::-1]
    return first_half == second_half or reverse_string == second_half
    

print(isPalindrome(word))