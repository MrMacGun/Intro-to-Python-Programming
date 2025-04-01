#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/12
#Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt".
#Each text file contains three rows with one word per row.
#Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

filename = input()

with open(filename, 'r') as file:
    words = file.readlines()
    
    w0 = words[0].strip()
    w1 = words[1].strip()
    w2 = words[2].strip()
    
    scent = f'{w0} {w1} {w2}'

with open(filename, 'a') as file:
    file.write(f"\n{scent}")
    
with open(filename, 'r') as file:
    update = file.read()
    
    print(update)