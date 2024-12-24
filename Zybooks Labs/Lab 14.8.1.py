file_name = input()
start_term = input()
final_term = input()

with open(file_name, 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        # whitespace is first stripped for comparison
        # (otherwise you could this behavior: 'millenium\n' <= 'millenium' 
        # as user inputs do not have \n on the end) and the file does.
        line = line.strip()

        # Simple range checks are used to see if the word should be output
        if ((start_term <= line) and (line <= final_term)):
            print(line, end='\n')