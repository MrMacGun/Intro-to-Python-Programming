#https://codingbat.com/prob/p153599
#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(s):
    # If the string has only one character, no need to swap
    if len(s) <= 1:
        return s
    else:
        # Swap the first and last characters
        return s[-1] + s[1:-1] + s[0]

print("Enter a string regardless of the size. the first and last characters will be switched")
print(front_back(str(input())))