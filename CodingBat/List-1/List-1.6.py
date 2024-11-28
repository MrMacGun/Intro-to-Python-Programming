#https://codingbat.com/prob/p148661
#Given an array of ints length 3, return an array with the elements "rotated left"
#so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  slice1 = nums[0]
  slice2 = nums[1]
  slice3 = nums[2]

  return slice2, slice3, slice1

print("Enter 3 numbers seperated via spaces and the program will roate the order of them")
userinput = input()
userlist = list(map(int, userinput.split()))

print(rotate_left3(userlist))