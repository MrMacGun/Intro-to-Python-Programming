#https://codingbat.com/prob/p135290
#Given an array of ints length 3, figure out which is larger, the first or last element in the array
#set all the other elements to be that value. Return the changed array.

def max_end3(nums):
    maxelement = max(nums)  # Find the maximum element in the list
    return [maxelement] * len(nums)  # Create a new list with the max element repeated

print("Input a list of 3 numbers, the program will determine the maxium muber and create a new list")
userinput = input()
userlist = list(map(int, userinput.split()))
print(max_end3(userlist))
