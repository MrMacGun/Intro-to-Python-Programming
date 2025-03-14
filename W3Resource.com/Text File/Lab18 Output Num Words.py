#https://www.w3resource.com/python-exercises/file/

filename = input("Enter File: ")
numword = 0

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        numword += len(words)

print("Number of words:", numword)