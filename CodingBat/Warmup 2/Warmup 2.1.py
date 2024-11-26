#https://codingbat.com/prob/p193507
#String is copied the number of tiems a string is inputted 

def string_times(str, n):
  return str * n

print("Enter a string and it will be repeated the number of times you enterd")
print(string_times(str(input()), int(input())))