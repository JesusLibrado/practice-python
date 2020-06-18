import hashlib 
  
print(hashlib.algorithms_available)

# initializing string 
str = input("Input: ")
  
# MD5
result = hashlib.md5(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of MD5 is: ") 
print(result.hexdigest())
  
print ("\r") 

# SHA1
result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 is: ") 
print(result.hexdigest())
  
print ("\r") 
  
# SHA256
result = hashlib.sha256(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is: ") 
print(result.hexdigest())
  
print ("\r") 