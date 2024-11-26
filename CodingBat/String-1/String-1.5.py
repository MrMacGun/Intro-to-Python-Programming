#https://codingbat.com/prob/p148853
#Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
#The string length will be at least 2.

def extra_end(str):
    newstr = str[-2:]
    return newstr * 3

print("Enter a string adn the last two characters will be repeated 3 times")
print(extra_end(str(input())))