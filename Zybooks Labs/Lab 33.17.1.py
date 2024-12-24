#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/17
#Write a program that reads integers user_num and div_num as input, and output the quotient (user_num divided by div_num).
#Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError and output an exception message.
#Use another except block to catch any ValueError caused by invalid input and output an exception message.


user_num = input()
div_num = input()

try:
    num1 = int(user_num)
    num2 = int(div_num)

    result = num1 // num2
    print(result)

except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")

except ValueError as e:
    print(f"Input Exception: {e}")