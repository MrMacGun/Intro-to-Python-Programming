#An user inputs a year adn the program outputs if it is a leap year or not
#The year must be divisable by 4
#If the year is a century year then it must be divisable by 400

is_leap_year = False

input_year = int(1600)

if input_year % 400 == 0:
    print(f"{input_year} - leap year")
    
elif input_year % 4 == 0 and input_year % 100 != 0:
    print(f"{input_year} - leap year")

else:
    print(f"{input_year} - not a leap year")