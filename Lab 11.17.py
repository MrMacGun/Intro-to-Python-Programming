#Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

user_int = 0

user_list = []

for i in user_list:
    if user_int >= 0:
        user_list.insert(user_int)
        user_int = int(input())
    elif user_int < 0:
        user_int = user_int * -1
        user_int = int(input())
    
print(user_list.sort)