#https://codingbat.com/prob/p192589
#Given an array of ints, return the sum of the first 2 elements in the array.
#If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
    slice1 = nums[0]
    slice2 = nums[1]
    newnum = slice1 + slice2
    return newnum

print("Enter a list of at least 2 numers and the first two numbers will be combined")
userint = input()
userlist = list(map(int, userint.split()))
print(sum2(userlist))