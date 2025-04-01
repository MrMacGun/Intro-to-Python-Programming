import csv
filename = input()
with open(filename, 'r', newline='') as file:
	rows = csv.reader(file)
	row1 = next(rows)
	row2 = next(rows)
	dict1 = {row1[i].strip(): row1[i+1].strip() for i in range(0, len(row1), 2)}
	dict2 = {row2[i].strip(): row2[i+1].strip() for i in range(0, len(row2), 2)}
	
print(dict1)
print(dict2)