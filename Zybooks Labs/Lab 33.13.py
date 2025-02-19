#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/13
#Prompt the user to enter a string of their choosing. Output the string. 
# Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. 
#Extend the program by calling the get_num_of_characters() function and then output the returned result.
#Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs)

print("Enter a sentence or phrase:")
uphra = input()
print("")
print(f'You entered: {uphra}')

def get_num_characters(uphra):
    count = 0
    for i in range(len(uphra)):
        count += 1
    return count
    
def output_without_whitespace(uphra):
    outphra = ""
    for i in uphra:
        if i != " " and i != "\n" and i != '\t':
            outphra += i
    return outphra 

print("")
print(f'Number of characters: {get_num_characters(uphra)}')
print(f'String with no whitespace: {output_without_whitespace(uphra)}')
