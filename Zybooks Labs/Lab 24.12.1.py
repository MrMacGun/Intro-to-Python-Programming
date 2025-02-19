#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/24/section/12

uint1 = int(input())
uint2 = int(input())
uint3 = int(input())
uint4 = int(input())

count = 0

if uint1 % 2 != 0:
    count += 1
if uint2 % 2 != 0:
    count += 1
if uint3 % 2 != 0:
    count += 1
if uint4 % 2 != 0:
    count += 1

print(count)

