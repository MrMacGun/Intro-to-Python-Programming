#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/4
#Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters.
#Output the exact area of the trapezoid in square meters as a float value.
b1 = int(input())
b2 = int(input())
h = int(input())

A = ((b1 + b2) / 2) * h

print("Trapezoid area:", A,"square meters")