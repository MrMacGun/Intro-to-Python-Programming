#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/12/section/7
#Write a program that calculates an adult's fat-burning heart rate, which is 70% of the difference between 220 and the person's age respectively
#Complete fat_burning_heart_rate() to calculate the fat burning heart rate.
#The adult's age must be between the ages of 18 and 75 inclusive. 
# If the age entered is not in this range, raise a ValueError exception in get_age() with the message "Invalid age."
#Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."

def get_age():
    age = int(input())
    validin = True
    if age < 18:
        print("Invalid Input")
    elif age > 75:
        print("Invalid Input")
    else:
        return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    220 - get_age
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    age = get_age()