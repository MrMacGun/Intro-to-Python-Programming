#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/7
#Create a solution that accepts an integer input to compare against the following list:
predef_list = [4, -27, 15, 33, -10]
#Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list

userint = int(input())
maxval = max(predef_list)

if userint > maxval:
    print("Greater Than Max? True")
elif userint < maxval:
    print("Greater Than Max? False")