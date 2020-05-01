word = input("Enter word: ")

def isPalindrome(input_string):
    return input_string == input_string[::-1]

print(isPalindrome(word))