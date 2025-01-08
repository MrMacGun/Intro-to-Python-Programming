#https://www.w3resource.com/python-exercises/file/

filename = input("Enter filename:")
ulist = []

with open(filename, "r") as file:
    for lines in file:
        ulist.append(lines.strip())

print("Lines for file")
print(ulist)
