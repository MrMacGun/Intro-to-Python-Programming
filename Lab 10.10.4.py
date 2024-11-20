# Complete the function to print all of the words in the given string
def printWords(mystring):
    userlist = mystring.split(' ')
    print(userlist)
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')