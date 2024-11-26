#https://codingbat.com/prob/p193604
#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  strlist = False
  if '1 2 3' in input_str:
    strlist = True
  return strlist

# Input handling
print("Input a set of numbers separated by spaces")
input_str = input()

print("Program determmines if the string containes 1 2 3 in sequence")
print(array123(input_str))