user_input = input()
lines = []
outfile = ''

# File IO block
with open(user_input, 'r') as file_in:
    lines = file_in.readlines()

# Replacing the string for each line to change names according to requirements.
for i in range(len(lines)):
    outfile += lines[i].replace('_photo.jpg', '_info.txt')

# Output only if there are lines, failure to put the print statement in an if
#   statement makes unit test fail, as eve        
if len(lines) != 0:
    print(outfile, end="")