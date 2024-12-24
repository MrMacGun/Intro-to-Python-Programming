input_file = input()
my_dict = {}
out_keys = 'output_keys.txt'
out_titles = 'output_titles.txt'
titles = []

# with open block takes in lines from the file
with open(input_file, 'r') as file_in:
    lines = file_in.readlines()

# For every other line read, (interval of 2)
#   Add the Key and the value inside a list to the dictionary if the key isn't already in the dictionary.
#   If the key is in the dictionary updates the key by appending the value to the existing value's list.
for i in range(0, len(lines), 2):
    # words from the line are stripped to prevent unwanted whitespace such as leading spaces or newlines (\n's) 
    #   from being entered into the dictionary.
    my_key = int(lines[i].strip())
    my_value = lines[i+1].strip()
    if my_key in my_dict:
        my_dict[my_key].append(my_value)
    else:
        my_dict[my_key] = [my_value]
    
    titles.append(my_value)

# Sorts the dictionary based on key (seasons run)
my_dict = sorted(my_dict.items())

out_str = ''


# This assembles a string to export output_keys.txt 
for i in range(len(my_dict)):
    out_str += str(my_dict[i][0])
    for j in range(len(my_dict[i][1])):
        sep_str = ': '
        if j > 0:
            sep_str = '; '
        out_str += sep_str + my_dict[i][1][j]
    out_str += '\n'

# Exports string into the output_keys.txt    
with open(out_keys, 'w') as file_out:
    file_out.write(out_str)
# print(out_str) # test outputs, no effect on grading, but I would disable 
# this on the real test.

# Builds string for output into out_titles.txt
out_str = ''
titles.sort()
for title in titles:
    out_str += title + '\n'
# print(out_str) # test outputs, no effect on grading, but I would disable 
# this on the real test.

# Exports string into out_titles.txt
with open(out_titles, 'w') as file_out:
    file_out.write(out_str)