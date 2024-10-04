frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

userindex = int(input())

if userindex <= -1:
    print("Error")
elif userindex >= 6:
    print("Error")
else:
    outputlist = frameworks[userindex]
    print(f'{outputlist}')

