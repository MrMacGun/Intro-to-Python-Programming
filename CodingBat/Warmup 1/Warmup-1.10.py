#https://codingbat.com/prob/p149524
#Given a non-empty string and an int n, return a new string where the char at index n has been removed.
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
  # Remove the character at index n by slicing the string into two parts
  return str[:n] + str[n+1:]

print("Input a string and then a number to index the string, that index will remove the letter")
print(missing_char(str(input()), int(input())))