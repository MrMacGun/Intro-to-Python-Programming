#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/21

def is_sorted_in_range():
    # Read the list of integers
    lst = list(map(int, input().split()))
    
    # Read the start and end positions (1-based index)
    start, end = map(int, input().split())
    
    # Convert to 0-based index for Python lists
    start -= 1
    end -= 1
    
    # Check if the sublist from start to end (inclusive) is sorted
    for i in range(start, end):
        if lst[i] > lst[i + 1]:
            print("no")
            return
    
    print("yes")

# Call the function
is_sorted_in_range()


