def steps_to_miles(steps):
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    return steps / 2000  # 2000 steps = 1 mile

# Main program
def main():
    try:
        # Read the number of steps from the user
        steps = int(input())
        
        # Call the steps_to_miles function and output the result
        miles = steps_to_miles(steps)
        print(f'{miles:.2f}')  # Print the miles with 2 decimal places

    except ValueError as e:
        # Catch any ValueError thrown by steps_to_miles and print the exception message
        print(e)

# Call the main function to run the program
if __name__ == "__main__":
    main()