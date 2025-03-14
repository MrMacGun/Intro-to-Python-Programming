filename = "F-35.txt"
line = int(input())

with open(filename, 'r') as file:
    lines = file.readlines()
    print("".join(lines[-line:]))
