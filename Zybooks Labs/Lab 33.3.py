#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/3
#Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.
#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:

quarters = (int(input()) * .25)
dimes = (int(input()) * .10)
nickels = (int(input()) * .05)
pennies = (int(input()) * .01)
dollars = quarters + dimes + nickels + pennies

print(f'Amount: ${dollars:.2f}')