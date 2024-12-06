#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/12
#Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt".
#Each text file contains three rows with one word per row.
#Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

# Step 1: Prompt the user for the text file name
filename = input()

# Step 2: Open the file in read mode to fetch the words
with open(filename, 'r') as file:
    lines = file.readlines()

# Ensure there are exactly three lines in the file
if len(lines) != 3:
    print("The file should contain exactly three lines of text.")
else:
    # Step 3: Retrieve the words and strip newline characters
    word1 = lines[0].strip()
    word2 = lines[1].strip()
    word3 = lines[2].strip()

    # Step 4: Form the sentence
    sentence = f"{word1} {word2} {word3}"

    # Step 5: Open the file in append mode and write the sentence
    with open(filename, 'a') as file:
        file.write(f"\n{sentence}")

    # Step 6: Output the updated file contents
    with open(filename, 'r') as file:
        updated_contents = file.read()

    # Output the file contents in the specified format
    print(updated_contents)