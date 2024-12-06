#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/2
#Create a solution that accepts an integer input representing any number of ounces.
#Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value.
#There are 16 ounces in a pound and 2,000 pounds in a ton.

#input in Ounces
userint = int(input())

#32000 ounces in 1 Tone
tons = userint//32000
midint = userint % 32000

#16 Ounces in 1 Lb
pounds = midint//16
ounces = midint%16

print("Tons:", tons)
print("Pounds:", pounds)
print("Ounces:", ounces)