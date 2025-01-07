#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/30/section/1
#Write a program that takes in three integers as inputs and outputs the largest value. 
#Use a try block to perform all the statements. Use an except block to catch any EOFErrors caused by missing inputs, output the number of inputs read, and output the largest value or "No max" if no inputs are read.

def main():
    count = 0
    numbers = []

    try:
        while count < 3:
            num= int(input())
            numbers.append(num)
            count = count + 1
        max_val = max(numbers)
        print(max_val)
    except EOFError:
        print(f'{count} input(s) read:')
        if count > 0:
            print(f'Max is {max(numbers)}')
        else:
            print("No max")

main()