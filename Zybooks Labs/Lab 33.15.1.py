#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/15
#Write a program to read dates from input, one date per line. 
#Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored. 
#The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.
def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int

while True:
    userstr = input().strip()
    
    # Exit condition
    if userstr == "-1":
        break
    
    # Validate if the date is in the correct format "Month Day, Year"
    parts = userstr.split()
    if len(parts) != 3:
        continue  # Skip if not exactly 3 parts (Month, Day, Year)
    
    month, day_year, year = parts
    day = day_year.split(',')[0]  # Extract day from "Day,"
    
    # Check if the month is valid
    month_int = get_month_as_int(month)
    if month_int == 0:
        continue  # Skip if month is invalid
    
    # Validate that day and year are numeric
    if not day.isdigit() or not year.isdigit():
        continue

    if "," not in userstr:
        continue
    
    # Print the formatted date
    print(f"{month_int}/{int(day)}/{year}")

