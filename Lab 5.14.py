#Lab 5.14
#Interstate Highway Numbers https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/5/section/14
#This lab is supposed to take an input of a number and output which type of highway it is (Either primary or alternate)
#Then this program will give the direction of the highway along with an invalid input text

highway_number = int(input())
    
if highway_number >= 1 and highway_number <= 99:
        # Primary highway logic
    if highway_number % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"
        
    print(f"I-{highway_number} is primary, going {direction}.")
    
elif highway_number >= 100 and highway_number <= 999:
       # Auxiliary highway logic
    primary_highway = highway_number % 100
        
    if primary_h+ighway == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        direction = "north/south" if primary_highway % 2 != 0 else "east/west"
        print(f"I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}.")
    
else:
    print(f"{highway_number} is not a valid interstate highway number.")

