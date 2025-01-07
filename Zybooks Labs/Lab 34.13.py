#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/13
#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
import csv

userfile = input()

with open(userfile, mode="r") as file:
    reader = csv.reader(file)
    # Step 3: Read the rows from the file and convert to dictionaries
    row1 = next(reader)
    row2 = next(reader)

    dict1 = {row1[i].strip(): row1[i+1].strip() for i in range(0, len(row1), 2)}
    dict2 = {row2[i].strip(): row2[i+1].strip() for i in range(0, len(row2), 2)}

print(dict1)
print(dict2)