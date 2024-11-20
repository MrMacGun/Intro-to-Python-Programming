#A predfined list exist, the user inputs a number
#The program checks if the input is greater than the user input value

predef_list = [4, -27, 15, 33, -10]

userint = int(input())

is_greater = True

for i in predef_list:
    if userint <= i:
        is_greater = False
        break  

if is_greater:
    print("Greater Than Max? True")
else:
    print("Greater Than Max? False")