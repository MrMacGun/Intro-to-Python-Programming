#https://codingbat.com/prob/p177892
#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    ifnum = False
    if (2 or 3) in nums:
        ifnum = True
        return ifnum
    else:
        return ifnum
    
print("Create an array, if 2 or 3 is in the array the program is true")
userint1 = input()
userlist1 = list(map(int, userint1.split()))
print(has23(userlist1))