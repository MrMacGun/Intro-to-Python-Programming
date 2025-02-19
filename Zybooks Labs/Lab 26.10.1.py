#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/26/section/10

def max_number(num1, num2, num3, num4):
    if (num1 > num2) and (num1 > num3) and (num1 > num4):
        return num1
    elif (num2 > num1) and (num2 > num3) and (num2 > num4):
        return num2
    elif (num3 > num1) and (num3 > num2) and (num3 > num4):
        return num3
    elif (num4 > num1) and (num4 > num2) and (num4 > num3):
        return num4
    elif (num1 == num2) and (num3 == num4):
        if num1 > num4:
            return num1
        else:
            return num4
    elif (num1 == num3) and (num2 == num4):
        if num1 > num2:
            return num1
        else:
            return num2
    
    
def min_number(num1, num2, num3, num4):
    if (num1 < num2) and (num1 < num3) and (num1 < num4):
        return num1
    elif (num2 < num1) and (num2 < num3) and (num2 < num4):
        return num2
    elif (num3 < num1) and (num3 < num2) and (num3 < num4):
        return num3
    elif (num4 < num1) and (num4 < num2) and (num4 < num3):
        return num4
    elif (num1 == num2) and (num3 == num4):
        if num1 < num4:
            return num1
        else:
            return num4
    elif (num1 == num3) and (num2 == num4):
        if num1 < num2:
            return num1
        else:
            return num2
    
    
if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    print(f'Maximum is {max_number(num1, num2, num3, num4)}')
    print(f'Minimum is {min_number(num1, num2, num3, num4)}')