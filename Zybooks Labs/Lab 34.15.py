#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/15
#Create a solution that accepts an integer input representing the age of a pig.
#Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig
#A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.

import pigAge

input_pig_age = int(input())
converted_pig_age = pigAge.pigAge_converter(input_pig_age)

print(input_pig_age ,'is', converted_pig_age, 'in human years')