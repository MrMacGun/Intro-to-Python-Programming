#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/14
#Create a solution that accepts an integer input
#Import the built-in module math and use its factorial() method to calculate the factorial of the integer input.
#Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.

import math

userint = int(input())
factorial = math.factorial(userint)

if factorial > 100:
    newbool = True
    print(factorial)
    print(newbool)
elif factorial < 100:
    newbool = False
    print(factorial)
    print(newbool)


