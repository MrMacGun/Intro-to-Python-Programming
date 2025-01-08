#https://www.w3resource.com/python-exercises/file/

filename = input("Enter Filename")
uvar = ""

with open(filename, "r") as file:
    for line in file:
        uvar += line

print(uvar)