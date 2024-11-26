#https://codingbat.com/prob/p166170
#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

# Input handling
print("Input a set of numbers separated by spaces")
input_str = input()
# Split the input string by spaces, convert each to an integer, and store them in the array
array = list(map(int, input_str.split()))

# Call the function and print the result
print("The program will determine the number of times 9 was inputted")
print(array_count9(array))