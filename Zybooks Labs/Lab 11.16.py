# Read input from the user
input_line = input()

# Convert the input string into a list of integers
numbers = list(map(int, input_line.split()))

# Compute the average and maximum
average = sum(numbers) / len(numbers)
maximum = max(numbers)

# Output the average and maximum
print(f"{average:.0f} {maximum}")