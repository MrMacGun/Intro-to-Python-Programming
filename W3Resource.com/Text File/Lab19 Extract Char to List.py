#https://www.w3resource.com/python-exercises/file/

filename = input("Enter the filename: ")
plist = []
charlist = []

# Get characters to match from the user until '!' is entered
while True:
    dchar = input("Enter character or word (or '!' to stop): ")
    if dchar == "!":
        break
    else:
        plist.append(dchar)  # Add the entered character or word to plist

# Open the file and check each character
with open(filename, "r") as file:
    for line in file:
        for char in line:  # Loop through each character in the line
            if char in plist:  # If the character is in plist, add it to charlist
                charlist.append(char)

# Print the list of characters found
print("Extracted characters:", charlist)
