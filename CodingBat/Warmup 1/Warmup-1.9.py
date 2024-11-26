#https://codingbat.com/prob/p189441
#Given a string, return a new string where "not " has been added to the front.
#However, if the string already begins with "not", return the string unchanged.

def not_string(s):
    # Check if the string starts with 'not'
    if s.startswith("not"):
        return s
    else:
        # Add 'not' at the beginning if it doesn't already start with it
        return "not " + s
  
print("Type an inpt, if the input does not begin with 'not', it will be added in")
print(not_string(str(input())))