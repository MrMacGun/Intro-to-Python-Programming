#https://codingbat.com/prob/p147920
#Given a string, we'll say that the front is the first 3 chars of the string.
#If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
  str = str[0:3]
  str = str * 3
  return str

print("Enter a string longer than 3 letters and it will be repeated 3 times")
print(front3(str(input())))