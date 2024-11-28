#https://codingbat.com/prob/p124806
#Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
#The original array will be length 1 or more.

def make_ends(nums):
    slice1 = nums[0]
    slice2 = nums[2]
    newlist = []
    newlist.append(slice1)
    newlist.append(slice2)
    return newlist

print("Enter a list and the first and last numbers will be added to the list")
userint1 = input()
userlist1 = list(map(int, userint1.split()))
print(make_ends(userlist1))