#https://codingbat.com/prob/p143951
#Given 3 int values, a b c, return their sum.
#However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
    # If all numbers are the same, return 0
    if a == b == c:
        return 0
    # If two numbers are the same, return the sum of the remaining one
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b
    # If all numbers are different, return their sum
    return a + b + c
  
print("Enter 3 numbners, if 2 of the numbers are the same the program outputs 0, if not the numbers will be added togther")
print(lone_sum(int(input()), int(input()), int(input())))