# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
    userlist = words
    userstr =' '.join(map(str,userlist))
    print(userstr)
    
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))