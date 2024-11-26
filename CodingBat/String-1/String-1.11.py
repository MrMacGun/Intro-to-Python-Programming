#https://codingbat.com/prob/p160545
#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end
#The string length will be at least 2.

def left2(str):
  if len(str) < 2:
    return print("Invalid input")
  elif len(str) > 2:
    strslice1 = str[0:2]
    strslice2 = str[2:]
    newstr = strslice2 + strslice1
    return newstr

print("Enter a string with a minimum of two characters")
print(left2(str(input())))