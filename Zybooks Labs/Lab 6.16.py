#''' Read in first equation, ax + by = c '''
a = int(8)
b = int(7)
c = int(38)

#''' Read in second equation, dx + ey = f '''
d = int(3)
e = int(-5)
f = int(-1)

def function_main(a, b, c, d, e, f):
    solution = False

x = type(int)
y = type(int)

if (a*x+b*y) == c and (d*x+e*y) == f:
    for x in range(-10, 11):
        for y in range(-10, 11):
            solution = True
            print(f"x = {x}, y = {y}")
            break

        if solution:
            False
            print("There is no solution")
            break
        
    if not solution:
        print("There is no solution")