#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/9

def calc_toll(hour, is_morning, is_weekend):
    toll = 0.0
    if is_morning == True and is_weekend == True:
        if hour < 7:
            toll = 1.05
            return toll
        elif hour >= 7 and hour < 12:
            toll = 2.15
            return toll
    elif is_morning == False and is_weekend == True:
        if hour >= 1 and hour < 8:
            toll = 2.15
            return toll
        elif hour >= 8:
            toll = 1.10
            return toll
    elif is_morning == True and is_weekend == False:
        if hour < 7:
            toll = 1.15
            return toll
        elif hour >= 7 and hour < 10:
            toll = 2.95
            return toll
        elif hour >= 10 and hour < 12:
            toll = 1.90
            return toll
    elif is_morning == False and is_weekend == False:
        if hour >= 1 and hour < 3:
            toll = 1.90
            return toll
        elif hour >= 3 and hour < 8:
            toll = 3.95
            return toll
        elif hour >= 8:
            toll = 1.40
            return toll

if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))