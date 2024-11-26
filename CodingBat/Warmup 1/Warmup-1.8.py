#https://codingbat.com/prob/p162058
#Given 2 int values, return True if one is negative and one is positive.
#Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  if (a < 0 and b > 0):
    if (negative == False):
        return True
  elif (a > 0 and b < 0):
    if (negative == False):
        return True
  elif ((a and b) < 0):
    if (negative == True):
        return True
  else:
    return False
  
print("Give two values, if one or both of the values is negative the program is true")
print(pos_neg((int(input())), (int(input())), ((bool(input())))))