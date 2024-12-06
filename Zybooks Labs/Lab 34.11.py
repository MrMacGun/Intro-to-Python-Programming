#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/11
#Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit
#The following dictionary purchase lists available items as the key with the cost per item as the value.
#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

userstr = str(input())
userint = int(input())

precost = purchase[userstr]
if userint in range(0, 11):
    cost = precost * userint
    print(f'{userstr} ${cost:.2f}')
elif userint in range(9, 21):
    cost = userint * (precost - (precost * .05)) 
    print(f'{userstr} ${cost:.2f}')
elif userint >= 21:
    cost = userint * (precost - (precost * .10)) 
    print(f'{userstr} ${cost:.2f}')
