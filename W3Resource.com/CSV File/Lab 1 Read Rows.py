import csv

filename = 'AFRC.csv'

with open(filename, 'r') as file:
    row = csv.reader(file)
    for x in row:
        print(row)