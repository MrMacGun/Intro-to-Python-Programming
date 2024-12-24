#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/13
#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
def get_num_of_characters(input_str):
    # note the count INCLUDES whitespace characters
    # they ask you to use a for loop, however you could simply
    # output len(input_str)
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def output_without_whitespace(input_str):
    #output string starts empty
    out_str = ''

    # for each char in the string
    for i in input_str:
        # if the character in the in string isn't a whitespace char
        # concatenate it to the end of the out string.
        if i != ' ' and i != '\n' and i != '\n' and i != '\t':
            out_str += i
    # after the for loop return the completed out string
    return out_str


if __name__ == '__main__':
    user_input = input('Enter a sentence or phrase:\n')
    print()
    print(f'You entered: {user_input}')
    print()
    print(f'Number of characters: {get_num_of_characters(user_input)}')
    print (f'String with no whitespace: {output_without_whitespace(user_input)}')