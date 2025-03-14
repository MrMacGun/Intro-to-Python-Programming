filename = input("Enter a file:")

print("Enter a list split via spaces")
uinp = input()
ulist = uinp.split() 

with open(filename, 'w') as file:
    file.write(' '.join(ulist))

with open(filename, 'r') as file:
    for line in file:
        print(line.strip())