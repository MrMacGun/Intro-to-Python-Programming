#https://codingbat.com/prob/p100347
#Given 3 int values, a b c, return their sum
#However, if any of the values is a teen -- in the range 13..19 inclusive
#then that value counts as 0, except 15 and 16 do not count as a teens.
#Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
#In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
#Define the helper below and at the same indent level as the main no_teen_sum().

def no_teen_sum(a, b, c):
  a = int(input())
  b = int(input())
  c = int(input())
  values = False
  if ((a or b or c) in range(13, 14)) or ((a or b or c) in range(17, 19)):
    if (a in range (13, 14)) or (a in range (17, 19)):
      a = 0
    if (b in range (13, 14)) or (b in range (17, 19)):
      b = 0
    if (c in range (13, 14)) or (c in range (17, 19)):
      c = 0
  elif ((a or b or c) in range(15,16)):
    n = 0
    def fix_teen(n):
      if (a in )
      n = n  % 2
      return values

  while ((a or b or c) not in range(13, 14)) 
  or ((a or b or c) not in range(17, 19)) or values == True:
    return a + b + c
  
print("Enter a series of numbers seperated via the enter the key")
print("If the number is between 13 and 19 it is excluded, except if it is 15 or 16 then it is modded 2")
print(no_teen((int(input())), int(input()), (int(input()))))
