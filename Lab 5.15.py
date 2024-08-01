# Lab 5.15
# This lab takes dates as input and outputs the date's season in the northern hemisphere
# The input begins with a string as the month and an integer as the day

input_month = 'March'
input_day = 3

spring_months = ('March', 'April', 'May', 'June')
summer_months = ('June', 'July', 'August', 'September')
autumn_months = ('September', 'October', 'November', 'December')
winter_months = ('December', 'January', 'February', 'March')

Month_List = ('March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February')

while input_day > 0 and input_day <= 31 and input_month in Month_List:
    if input_month in spring_months:
        if (input_month == 'March' and 20 <= input_day <= 31) or \
           (input_month == 'April' and 1 <= input_day <= 30) or \
           (input_month == 'May' and 1 <= input_day <= 31) or \
           (input_month == 'June' and 1 <= input_day <= 20):
            print('Spring')
    
    elif input_month in summer_months:
        if (input_month == 'June' and 21 <= input_day <= 30) or \
           (input_month == 'July' and 1 <= input_day <= 31) or \
           (input_month == 'August' and 1 <= input_day <= 31) or \
           (input_month == 'September' and 1 <= input_day <= 21):
            print('Summer')
    
    elif input_month in autumn_months:
        if (input_month == 'September' and 22 <= input_day <= 30) or \
           (input_month == 'October' and 1 <= input_day <= 31) or \
           (input_month == 'November' and 1 <= input_day <= 30) or \
           (input_month == 'December' and 1 <= input_day <= 21):
            print('Autumn')
    
    elif input_month in winter_months:
        if (input_month == 'December' and 22 <= input_day <= 31) or \
           (input_month == 'January' and 1 <= input_day <= 31) or \
           (input_month == 'February' and 1 <= input_day <= 28) or \
           (input_month == 'March' and 1 <= input_day <= 19):
            print('Winter')
    
    else:
        print('Invalid')

else:
    print('Invalid')