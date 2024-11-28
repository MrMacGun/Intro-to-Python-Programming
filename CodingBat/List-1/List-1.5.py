#https://codingbat.com/prob/p191645
#Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  slice1 = nums[0]
  slice2 = nums[1]
  slice3 = nums[2]

  return slice1 + slice2 + slice3

print("Enter a list of three numbers seperated via spaces, and the elements will be added togther")
userinput = input()
userlist = list(map(int, userinput.split()))

print(sum3(userlist))