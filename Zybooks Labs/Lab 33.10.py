#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/10
#Write a program that takes in a line of text as input, and outputs that line of text in reverse. 
#The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

while True:
    userstr = input()  
    if userstr == 'done' or userstr == 'Done' or userstr == 'd':
        break  
    else:
        newstr = userstr[::-1] 
        print(newstr)  
