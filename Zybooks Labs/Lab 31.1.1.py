#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/31/section/1
#Given a text file containing the availability of food items, write a program that reads the information from the text file and outputs the available food items. 
#The program first reads the name of the text file from the user. The program then reads the text file, stores the information into four separate lists, and outputs the available food items in the following format: name (category) -- description
#Assume the text file contains the category, name, description, and availability of at least one food item, separated by a tab character ('\t').

filename = input().strip().lower()
catagories = []
names = []
descriptions = []
availablility = []

with open(f'{filename}', 'r') as file:
    for lines in file:
        parts = lines.strip().split('\t')

        if len(parts) == 4:
            catagory, name, description, avail = parts
            catagories.append(catagory)
            names.append(name)
            descriptions.append(description)
            availablility.append(avail)
    
    for i in range(len(names)):
        if availablility[i] == "Available":
            print(f"{names[i]} ({catagories[i]}) -- {descriptions[i]}")

