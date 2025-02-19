#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/14

float1 = float(input())
float2 = float(input())
epsilon = float(input())

difference = abs(float1 - float2)

if difference < 0.001:
    print("equal")
elif difference < epsilon:
    print("close enough")
else:
    print("not close")
