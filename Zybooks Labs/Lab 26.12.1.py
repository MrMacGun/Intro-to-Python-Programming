#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/12

# Function to print the menu
def print_menu():
    print("")
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")

# Function to execute menu option
def execute_menu(choice, text):
    if choice == 'c':
        print("Number of non-whitespace characters:", get_num_of_non_WS_characters(text))
    elif choice == 'w':
        print("Number of words:", get_num_of_words(text))
    elif choice == 'f':
        num_capitalized, edited_text = fix_capitalization(text)
        print(f"Number of letters capitalized: {num_capitalized}")
        print("Edited text:", edited_text)
    elif choice == 'r':
        exclamation_count, semicolon_count, edited_text = replace_punctuation(text)
        print(f"Punctuation replaced\nexclamation_count: {exclamation_count}\nsemicolon_count: {semicolon_count}")
        print("Edited text:", edited_text)
    elif choice == 's':
        edited_text = shorten_space(text)
        print("Edited text:", edited_text)

# Function to get the number of non-whitespace characters
def get_num_of_non_WS_characters(text):
    return len([char for char in text if not char.isspace()])

# Function to get the number of words in the string
def get_num_of_words(text):
    words = text.split()
    return len(words)

# Function to fix capitalization: Capitalizes first letter of each sentence
def fix_capitalization(text):
    sentences = text.split('. ')
    num_capitalized = 0
    edited_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence[0].islower():
            num_capitalized += 1
            edited_sentences.append(sentence[0].upper() + sentence[1:])
        else:
            edited_sentences.append(sentence)
    
    edited_text = '. '.join(edited_sentences)
    return num_capitalized, edited_text

# Function to replace punctuation
def replace_punctuation(text):
    exclamation_count = text.count('!')
    semicolon_count = text.count(';')
    
    # Replace '!' with '.' and ';' with ','
    edited_text = text.replace('!', '.').replace(';', ',')
    
    return exclamation_count, semicolon_count, edited_text

# Function to shorten spaces
def shorten_space(text):
    while '  ' in text:  # While there are two or more spaces
        text = text.replace('  ', ' ')
    return text

# Main program loop
def main():
    # Step 1: Prompt user for input text
    text = input("Enter a sample text:\n")
    print("\nYou entered:", text)
    
    # Step 2: Display menu and prompt user for option
    while True:
        print_menu()
        choice = input("\nChoose an option:\n").lower()

        # Quit the program if the user selects 'q'
        if choice == 'q':
            break
        # Otherwise, process the menu choice
        elif choice in ['c', 'w', 'f', 'r', 's']:
            execute_menu(choice, text)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
