#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/8
#Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
#Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

userint = (int(input()))


if userint in range(0, 6):
    output = frameworks[userint]
    print(output)
else:
    print("Error")