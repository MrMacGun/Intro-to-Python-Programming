frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input


try:
    uint = int(input())
    print(frameworks[uint])
except EOFError:
    print("Error")
except IndexError:
    print("Error")