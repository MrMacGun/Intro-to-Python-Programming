import csv

def main():
    # Read the file name from the user
    filename = input().strip()
    
    # Create a dictionary to store word frequencies
    word_count = {}
    
    try:
        # Open the file for reading
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            # Process each row in the CSV file
            for row in reader:
                for word in row:
                    word = word.strip()  # Clean any extra spaces around the word
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
        # Output the words and their frequencies
        for word, count in word_count.items():
            print(f"{word} {count}")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
        
# Run the program
if __name__ == "__main__":
    main()
