#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/9
#Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer

userint1 = int(input())
userint2 = int(input())

if userint1 > userint2:
    print("Second integer can't be less than the first.")
else:
    newlist = []
    
    while userint1 <= userint2:
        newlist.append(userint1)
        userint1 += 5  

    print(*newlist,"")

    