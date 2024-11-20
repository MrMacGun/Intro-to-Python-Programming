# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
    if 'WGU' in mystring:
        mystring = mystring.replace('WGU','Western Governors University')
        print(mystring)
    
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')