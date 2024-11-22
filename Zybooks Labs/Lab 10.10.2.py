# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    x = str(input())
    print('WGU College of IT', len(x))
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))