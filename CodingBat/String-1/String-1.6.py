#https://codingbat.com/prob/p184816
#Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
#If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
  if len(str) >= 2:
    newline1 = str[0:2]
    return newline1
  elif len(str) < 2:
    newline1 = str[0:1]
    return newline1
  else:
    return ""
  
print("Enter a string, the first two letters will be extracted")
print(first_two(str(input())))