#https://codingbat.com/prob/p192962
#Given an array of ints length 3, return a new array with the elements in reverse order
#so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
  slice1 = nums[0]
  slice2 = nums[1]
  slice3 = nums[2]

  return slice3, slice2, slice1

print("Enter 3 numbers seperated via spaces and the program will reverse the order")
userinput = input()
userlist = list(map(int, userinput.split()))

print(reverse3(userlist))