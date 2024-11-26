#https://codingbat.com/prob/p127703
#Given 2 strings, return their concatenation, except omit the first char of each.
#The strings will be at least length 1.

def non_start(a, b):
  newa = a[1:]
  newb = b[1:]
  newstring = newa + newb

  return newstring

print("Enter two strings seperated via the enter key, both strings will have the first charactor removed")
print(non_start(str(input()), str(input())))