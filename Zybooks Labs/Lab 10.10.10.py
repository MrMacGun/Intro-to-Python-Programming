# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    count = 0
    for i in mystring:
        if(i.isupper()):
            count += 1
    print(count)
 
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))