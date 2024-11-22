def near_hundred(n):
    if n in range (90, 110) or n in range (190, 210):
        return True
    else:
        return False
    
print("input a number, if it's +-10 of 100 or 200 it's true")
print(near_hundred(int(input())))