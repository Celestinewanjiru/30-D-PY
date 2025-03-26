def is_palindrome(s):
  return s == s[::1]

#ask for input
input_string = input("enter a string: ")

#check if string is palindrome
if is_palindrome(input_string):
  print(f"{input_string} is palindrome")
else:
  print(f"{input_string} is not palindrome try another one")