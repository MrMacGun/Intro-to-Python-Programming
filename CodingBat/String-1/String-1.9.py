#https://codingbat.com/prob/p194053
#Given 2 strings, a and b, return a string of the form short+long+short
#with the shorter string on the outside and the longer string on the inside
#The strings will not be the same length, but they may be empty (length 0)

def combo_string(a, b):
  if len(a) == 0 or len(b) == 0:
        return 'Invalid input'
  if len(a) > len(b):
        newstr = b + a + b  # shorter string is b, longer string is a
  else:
        newstr = a + b + a  # shorter string is a, longer string is b
  return newstr

  
print("Enter two strings, one string must be smaller than the other but cannot equal 0")
print(combo_string(str(input()), str(input())))