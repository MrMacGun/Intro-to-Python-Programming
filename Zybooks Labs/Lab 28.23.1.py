#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/23

def is_palindrome(lst):
    """Return True if the list is a palindrome, else False."""
    return lst == lst[::-1]

def find_mode(lst):
    """Return the mode of the list (the number that appears most often)."""
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    # Find the number with the maximum frequency
    mode = max(frequency, key=frequency.get)
    return mode

# Main portion of the program
if __name__ == '__main__':
    # Step 0: Read the input list of integers
    lst = list(map(int, input().split()))
    
    # Step 1: Minimum and Maximum values
    min_val = min(lst)
    max_val = max(lst)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    
    # Step 2: Calculate the mean
    total_sum = sum(lst)
    mean = total_sum / len(lst)
    print(f"Mean: {mean:.1f}")
    
    # Step 3: Check if the list is a palindrome
    palindrome = is_palindrome(lst)
    print(f"Palindrome: {palindrome}")
    
    # Step 4: Calculate the median
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    if n % 2 == 1:  # Odd length, median is the middle element
        median = lst_sorted[n // 2]
    else:  # Even length, median is the average of the two middle elements
        median = (lst_sorted[n // 2 - 1] + lst_sorted[n // 2]) / 2
    print(f"Median: {median:.1f}")
    
    # Step 5: Find the mode
    mode = find_mode(lst_sorted)
    print(f"Mode: {mode}")
