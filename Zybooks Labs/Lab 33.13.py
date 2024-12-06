#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/13
#Prompt the user to enter a string of their choosing. Output the string. 
# Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. 
#Extend the program by calling the get_num_of_characters() function and then output the returned result.
#Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs)

print("Enter a sentence or phrase:")
userstr = str(input())
print(userstr)

def get_num_of_characters(input_str):
    newstr = input_str.repalce(" ","")
    return newstr


if __name__ == '__main__':
    print("You entered:",userstr)
    print("")
    print("Number of characters: ", len(get_num_of_characters(userstr)))
    print("String with no whitespace: ",get_num_of_characters(userstr))
