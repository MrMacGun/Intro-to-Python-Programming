#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/12/section/8
#12.8 LAB: Exception handling to detect input string vs. integer
#The given program reads a list of single-word first names and ages (ending with -1), and outputs that list with the age incremented. 
#The program fails and throws an exception if the second input on a line is a string rather than an integer.
#At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.

parts = input().split()
name = parts[0]
while name != '-1':
     # try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
    except:
        age = 0
    print(f'{name} {age}')
    
    # Get next line
    parts = input().split()
    name = parts[0]