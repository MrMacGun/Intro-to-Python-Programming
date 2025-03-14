#https://www.w3resource.com/python-exercises/file/
filename = 'F-35.txt'

with open(filename, 'r') as file:
    for line in file:
        print(line)