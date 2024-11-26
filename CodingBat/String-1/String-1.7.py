#https://codingbat.com/prob/p107010
#Given a string of even length, return the first half.
#So the string "WooHoo" yields "Woo"

def first_half(str):
  strlength = len(str) // 2
  newstr = str[0:strlength]
  return newstr

print("Enter a string and half of the string will be returned")
print(first_half(str(input())))