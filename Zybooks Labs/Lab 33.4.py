#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/4
#Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input
#output the gas cost for 20 miles, 75 miles, and 500 miles.

miles_per_gallon = float(input())
dollars_per_gallon = float(input())
miles_20 = (20/miles_per_gallon) * dollars_per_gallon
miles_75 = (75/miles_per_gallon) * dollars_per_gallon
miles_500 = (500/miles_per_gallon) * dollars_per_gallon

print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')