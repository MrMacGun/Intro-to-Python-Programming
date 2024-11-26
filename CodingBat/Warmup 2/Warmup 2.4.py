#https://codingbat.com/prob/p118366
#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]  # Add the substring from the start to the current position
    return result

print("enter a string to repeat the string a set number of times")
print(string_splosion(str(input())))