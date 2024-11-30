#https://codingbat.com/prob/p129125
#You and your date are trying to get a table at a restaurant.
#The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes.
#The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
#If either of you is very stylish, 8 or more, then the result is 2 (yes).
#With the exception that if either of you has style of 2 or less, then the result is 0 (no).
#Otherwise the result is 1 (maybe).

def date_fashion(you, date):
  entrance = 0
  if (you >= 5) and (date >= 5):
    entrance += 1
    return entrance
  elif ((you >= 10) or (date >= 10)) and ((you >= 5) and (date >= 5)):
    entrance += 2
    return entrance
  else:
    return entrance

print("You've made a mistake and decided to go to a resturant with a date that has attier requirements")
print("You are getting graded by a washed up 3N0X6 about how your outfit looks")
print("You and Jodies outfit will be rated in a scale of 1-10 and the bouncer will grade you between 1-3")
print("If your outfits are graded below 5 they might not let you in, so it's time to stop by the local VFW")
print("The bouncer only talks in variables between 1 - 3 (Might be a burn pit or something).")
print(" 0 they one let you in, 1 they might, and 2 you got a good ASVAB score")
print("Enter the two numbers the bouncer graded you seperated via the enter key")
you = int(input())
date = int(input())
print(date_fashion(you, date))