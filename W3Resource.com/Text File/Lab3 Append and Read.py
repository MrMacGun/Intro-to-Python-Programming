#https://www.w3resource.com/python-exercises/file/

filename = input("Enter File:")

with open(filename, 'w') as file:
    usinp = input("Enter text:")
    file.write(usinp)

with open(filename, 'r') as file:
    for line in file:
        print(line)