#https://codingbat.com/prob/p182414
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    count = 0
    # Loop through the strings, stopping before the last character to avoid index out of range
    for i in range(len(a) - 1):
        # Create 2-character substrings from both strings at the same index
        if i < len(b) - 1 and a[i:i+2] == b[i:i+2]:
            count += 1
    return count

# Input handling
print("Enter two strings, if every two characters are matching, the counter increases.")
a = input("Enter first string: ")
b = input("Enter second string: ")

# Call the function and print the result
print(string_match(a, b))