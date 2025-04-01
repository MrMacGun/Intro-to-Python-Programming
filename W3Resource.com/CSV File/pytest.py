import csv
filename = 'book1.xlsx'

with open(filename, 'r', newline='') as file:
	rows = csv.reader(file)
	row1 = rows
	row2 = rows
	    
	dict1 = {row1[i].split(): row1[i+1].split() for i in range(0, len(row1), 2)}
	dict2 = {row2[i].split(): row2[i+1].split() for i in range(0, len(row2), 2)}
	    
print(dict1)
print(dict2)