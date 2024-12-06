#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/5

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

sumnumint = num1 + num2 + num3 + num4 + num5
sumnumfloat = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)
sumnumstr = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f'Integer: {sumnumint}')
print(f'Float: {sumnumfloat:.1f}')
print(f'String: {sumnumstr}')