#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/11/section/20
#Write the in_order() function, which has a list of integers as a parameter, and returns True if the integers are sorted (in order from low to high) or False otherwise. 
#The program outputs "In order" if the list is sorted, or "Not in order" if the list is not sorted.

userlist = [int(x) for x in input().split()]

def in_order(nums):
    if nums == sorted(nums):
        print('In order')
    else:
        print("Not in order")
    
print(in_order(userlist))
