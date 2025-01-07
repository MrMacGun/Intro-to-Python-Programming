#https://www.w3resource.com/python-exercises/file/
#Read the first line in the file
filename = input()

with open(filename, 'r') as file:
    firstline = file.readline()
    print(firstline)

    