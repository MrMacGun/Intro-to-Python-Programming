#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/6
#Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. 

userinput = input()

slice1 = userinput[0:3]
slice2 = userinput[3:5]
slice3 = userinput[5:9]

phonenum = slice1 + "-" + slice2 + "-" + slice3
print(phonenum)