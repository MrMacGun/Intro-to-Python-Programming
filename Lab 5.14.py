#Lab 5.14
#Interstate Highway Numbers https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/5/section/14
#This lab is supposed to take an input of a number and output which type of highway it is (Either primary or alternate)
#Then this program will give the direction of the highway along with an invalid input text

highway_number = int(input())
pri_hw = 0
alt_hwSub = 0
atl_hw = 0
IncorrectDig = int('200')

#Renoves invalid inputs
if highway_number <= 0 or highway_number == 200:
    print(highway_number,'is not a valid interstate highway number.')
#Detects if the highway number is within the range of the input number
if highway_number <= 99 and highway_number <= 1:
    pri_hw = str(highway_number) 
    
#Checks Directional Heading
elif '5' in pri_hw[1]:
    print('I-',pri_hw, 'is primary, going north/south')
#Checks Directional Heading
else: '0' in pri_hw[1]
print('I-',pri_hw, 'is primary, going east/west.')
#Checks for alternate highway
if highway_number <=100 and highway_number >=999:
    alt_hwSub = atl_hw - 100
    atl_hw = str(highway_number)
#Checks Directional Heading
elif '5' in atl_hw[1]:
    print('I-',atl_hw, 'is alternate,serving I-',alt_hwSub,', going north/south.')
#Checks Directional Heading
else: '0' in atl_hw[1]
print('I-',atl_hw, 'is alternate,serving I-',alt_hwSub,', going east/west.')

