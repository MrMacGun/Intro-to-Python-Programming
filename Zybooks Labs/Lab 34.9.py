#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/9
#Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit.

usertemp = int(input())

if usertemp >= 212:
    print("Boiling")
    print("Caution: Hot!")
elif 115 < usertemp < 211:
    print("Hot")
elif 80 < usertemp <= 115:
    print("Warm")
elif 33 <= usertemp <= 80:
    print("Cold")
elif usertemp < 33:
    print("Frozen")
    print("Watch out for ice!")