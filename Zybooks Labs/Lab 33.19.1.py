def main():
    # Read the word and the letter from the user
    word = input().strip().lower()  # The word for which we want to find synonyms
    letter = input().strip().lower()  # The letter to filter synonyms by
    
    # Initialize the dictionary to store synonyms by their starting letter
    synonyms_dict = {}
    
    # Open the file named after the word
    try:
        with open(f'{word}.txt', 'r') as file:
            # Process each line in the file
            for line in file:
                # Split the line into synonyms
                synonyms = line.split()
                
                # Process each synonym and categorize by the first letter
                for synonym in synonyms:
                    first_letter = synonym[0].lower()
                    if first_letter not in synonyms_dict:
                        synonyms_dict[first_letter] = []
                    synonyms_dict[first_letter].append(synonym.lower())
    
        # Check if there are any synonyms starting with the given letter
        if letter in synonyms_dict and synonyms_dict[letter]:
            for synonym in synonyms_dict[letter]:
                print(synonym)
        else:
            print(f"No synonyms for {word} begin with {letter}.")
    
    except FileNotFoundError:
        print(f"File {word}.txt not found.")

# Call the main function
if __name__ == "__main__":
    main()
