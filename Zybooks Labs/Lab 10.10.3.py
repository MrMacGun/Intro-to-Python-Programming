# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
    if 'WGU' in mystring:
        print('True')
    elif 'WGU' != mystring:
        print('False')
    
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))