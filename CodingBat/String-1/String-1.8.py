#https://codingbat.com/prob/p138533
#Given a string, return a version without the first and last char, so "Hello" yields "ell".
#The string length will be at least 2.

def without_end(str):
  strslice = str[1:-1]
  return strslice

print("Enter a string minimum 3 characters and the first and last charcharts are omitted")
print(without_end(str(input())))