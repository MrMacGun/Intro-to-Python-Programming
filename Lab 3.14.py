#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/3/section/14
#Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z)
#the absolute value of (x minus y), and the square root of (x to the power of z).


import math

x = float(input())
y = float(input())
z = float(input())


Num1 = x**z
Num2 = x ** (y**z)
Num3 = abs(x - y)
Num4 = math.sqrt(x ** z)

print(f'{Num1:.2f} {Num2:.2f} {Num3:.2f} {Num4:.2f}')