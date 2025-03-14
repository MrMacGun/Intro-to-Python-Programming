#https://www.w3resource.com/python-exercises/file/

filename = input("Enter File:")

ulist = []
maxl = 0

with open(filename, "r") as file:
    for line in file:
        line = line
        if len(line) > maxl:
            maxl - len(line)
    
print(max(ulist))
