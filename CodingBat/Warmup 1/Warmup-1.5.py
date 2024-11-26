#https://codingbat.com/prob/p166884
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if hour in range(7, 20) and talking == True:
        return True
    else:
        return False

print("A parrot likes to talk a lot, it shouldn't be talking from before 7 or after 2000")
print("Enter two inputs, if the parrot is or isn't talking enter True or False")
print("Enter the hour the parrort is talking")

print(parrot_trouble(bool(input()), int(input())))