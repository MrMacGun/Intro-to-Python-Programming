#https://codingbat.com/prob/p165097

def front3(str):
  str = str[0:3]
  str = str * 3
  return str

print("Enter a string longer than 3 letters and it will be repeated 3 times")
print(front3(str(input())))