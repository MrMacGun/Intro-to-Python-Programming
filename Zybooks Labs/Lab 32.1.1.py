

def draw_triangle(base_length):
    for i in range(base_length):
        for j in range(i):
            print(" ",end="")
        for j in range(base_length - i):
            print("*", end="")
        print()
if __name__ == '__main__':
    base_length = int(input())  
    draw_triangle(base_length)
