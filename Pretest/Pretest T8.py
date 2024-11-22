#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature

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