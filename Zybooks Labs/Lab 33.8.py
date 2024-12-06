#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/7
#Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line
#The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

uint = int(input())

if uint <= 0:
    print("No change")
else:
    
    dollars = uint // 100
    if dollars == 1:
        print(dollars, "Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")
     
    remaining = uint % 100
    
    quarters = remaining // 25
    if quarters == 1:
        print(quarters, "Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")
    
    remaining = remaining % 25
    
    dimes = remaining // 10
    if dimes == 1:
        print(dimes, "Dime")
    elif dimes > 1:
        print(dimes, "Dimes")
    
    remaining = remaining % 5

    nickel = remaining
    if nickel == 1:
        print(nickel, "Nickel")
    elif nickel > 1:
        print(nickel, "Nickels")
    
    pennies = remaining
    if pennies == 1:
        print(pennies, "Penny")
    elif pennies > 1:
        print(pennies, "Pennies")
