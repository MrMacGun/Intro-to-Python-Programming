#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/12/section/7
#Write a program that calculates an adult's fat-burning heart rate, which is 70% of the difference between 220 and the person's age respectively
#Complete fat_burning_heart_rate() to calculate the fat burning heart rate.
#The adult's age must be between the ages of 18 and 75 inclusive. 
# If the age entered is not in this range, raise a ValueError exception in get_age() with the message "Invalid age."
#Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."

def get_age():
    try:
        age = int(input())  # Prompt for age input
        # Check if age is within the valid range (18 to 75 inclusive)
        if 18 <= age <= 75:
            return age
        else:
            raise ValueError("Invalid age.")  # If the age is out of range, raise an exception
    except ValueError:
        # If age is invalid, raise an error with a custom message
        raise ValueError("Invalid age.\nCould not calculate heart rate info.")

def fat_burning_heart_rate(age):
    # Fat burning heart rate is calculated as 70% of the difference between 220 and the age
    heart_rate = (220 - age) * 0.70
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()  # Get age from user input
        heart_rate = fat_burning_heart_rate(age)  # Calculate heart rate
        print(f'Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm')
    except ValueError as e:
        print(e)  # Print the error message if the age is invalid
