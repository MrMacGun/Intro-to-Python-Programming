import csv

filename = 'MOCK_DATA.csv'
new_list = []

with open(filename, 'r') as file:
    reader = file.readlines()
    line_5 = reader[4].strip()
    new_list = line_5.split(",")

for x in reversed(new_list):
    print(x)
