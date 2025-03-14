#https://www.w3resource.com/python-exercises/file/
#Read the first line in the file
filename = "F-35.txt"
lines = int(input())

with open(filename, 'r') as file:
    for i in range(lines):
        line = file.readline()
        if not line:
            break
        print(line, end='')

    