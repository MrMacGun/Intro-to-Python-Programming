# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    s = mystring.split()
    if s[0] == "WGU":
        return mystring
    else:
        return mystring.replace("WGU","")
        
    print(removeWGU)
    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))