#https://codingbat.com/prob/p100347
#Given 3 int values, a b c, return their sum
#However, if any of the values is a teen -- in the range 13..19 inclusive
#then that value counts as 0, except 15 and 16 do not count as a teens.
#Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
#In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
#Define the helper below and at the same indent level as the main no_teen_sum().

def fix_teen(n):
    # If the number is a teen (13-19) but not 15 or 16, return 0
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n

def no_teen_sum(a, b, c):
    # Apply the fix_teen function to each value
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    
    # Return the sum of the adjusted values
    return a + b + c

  
print("Enter a series of numbers seperated via the enter the key")
print("If the number is between 13 and 19 it is excluded, except if it is 15 or 16 then it is modded 2")
print(no_teen_sum((int(input())), int(input()), (int(input()))))
