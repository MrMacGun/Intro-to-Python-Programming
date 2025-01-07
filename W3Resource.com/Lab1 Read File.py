#https://www.w3resource.com/python-exercises/file/
filename = input()

with open(filename, 'r') as file:
    for line in file:
        print(line)