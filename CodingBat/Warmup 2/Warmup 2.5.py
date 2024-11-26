#https://codingbat.com/prob/p145834
#Given a string, return the count of the number of times that a substring length 2 appears in the string
#and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(s):
    if len(s) < 2:
        return 0
    
    # Take the first two characters
    first_two = s[:2]
    count = 0
    
    # Loop through the string (excluding the last two characters)
    for i in range(len(s) - 2):
        if s[i:i+2] == first_two:
            count += 1
    
    return count
    
print("Enter a string, the program will count the number of times the first two charcaters are in the string")
print(last2(str(input())))
    