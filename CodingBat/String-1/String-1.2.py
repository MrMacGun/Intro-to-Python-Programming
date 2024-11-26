#https://codingbat.com/prob/p182144
#Given two strings, a and b, return the result of putting them together in the order abba
#e.g. "Hi" and "Bye" returns "HiByeByeHi"

def make_abba(a, b):
    newstr = a + b + b + a
    return newstr

print("enter two strings seperated by the enter key")
print(make_abba((str(input())), (str(input()))))