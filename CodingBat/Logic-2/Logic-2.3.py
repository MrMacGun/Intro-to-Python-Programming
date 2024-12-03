#https://codingbat.com/prob/p107863
#Given 3 int values, a b c, return their sum.
#However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
#So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
    # If a is 13, return 0 (exclude a, b, and c)
    if a == 13:
        return 0
    # If b is 13, return the sum of a (exclude b and c)
    if b == 13:
        return a
    # If c is 13, return the sum of a and b (exclude c)
    if c == 13:
        return a + b
    # If none of them are 13, return the sum of a, b, and c
    return a + b + c

print("Enter as et of 3 number seperated via the enter key")
print("If 13 is in the set, all following numbers will be 0")
print(lucky_sum(int(input()), int(input()), int(input())))