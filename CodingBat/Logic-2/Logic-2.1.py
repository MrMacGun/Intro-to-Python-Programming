#https://codingbat.com/prob/p118406
#We want to make a row of bricks that is goal inches long. 
#We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#Return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
  bigL = big * 5
  count  = small + bigL
  if count == goal:
    return True
  else:
    return False
  
print("You have a set of bricks, small bricks and large bricks")
print("The small bricks are 1in long and the large bricks are 5in long")
print("Enter a goal length you're trying to achive and the combination of bricks seperated via the enter key")

print(make_bricks((int(input())), (int(input())), (int(input()))))