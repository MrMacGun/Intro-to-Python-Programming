#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/11
#The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two
#ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence
#Any negative index values should return -1.

def fibonacci(n):
    # Handle the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return -1

    # Iterative approach for n >= 2
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update a to b, and b to a + b

    return b

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')