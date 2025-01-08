#https://www.w3resource.com/python-exercises/file/

filename = input("Enter File:")

with open(filename, 'r') as file:
    for line in reversed(file.readlines()):
        print("This is the last line of the File:")
        print(line)
        break