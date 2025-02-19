#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/22

def read_customer_data(filename):
    """Read and return data from filename as a list of lists (name, state, debt)"""
    names = []
    states = []
    debts = []

    with open(filename) as f:
        rows = f.readlines()
    for row in rows:
        row = row.split(',')
        names.append(row[0])
        states.append(row[1])
        debts.append(float(row[2].strip()))  # Convert debt to float for accurate comparisons
    return names, states, debts

# Main portion of the program
if __name__ == '__main__':
    # number of rows to consider
    num_customers = int(input())
    
    # Read customer data
    names, states, debts = read_customer_data("CustomerData.csv")

    # Step 1: Get inputs for debt limit, search phrase, and state abbreviation
    debt_limit = float(input())  # Read the debt limit as float for accurate comparison
    search_phrase = input()  # The search string for name filtering
    state_abbr = input()  # The state abbreviation for state-specific statistics

    # Step 2: Find customer with the highest debt
    highest_debt = -1
    highest_debt_name = ""
    for i in range(num_customers):  # Only consider the specified number of customers
        if debts[i] > highest_debt:
            highest_debt = debts[i]
            highest_debt_name = names[i]
    
    # Output the U.S. report
    print("U.S. Report")
    print(f"Customers: {num_customers}")
    print(f"Highest debt: {highest_debt_name}")
    
    # Step 3: Count customer names that start with the search phrase
    search_count = 0
    for name in names[:num_customers]:  # Only consider the specified number of customers
        if name.startswith(search_phrase):
            search_count += 1
    
    print(f"Customer names that start with \"{search_phrase}\": {search_count}")
    
    # Step 4: Count customers with debt higher than the limit and those who are debt-free
    over_limit_count = 0
    debt_free_count = 0
    for debt in debts[:num_customers]:  # Only consider the specified number of customers
        if debt > debt_limit:
            over_limit_count += 1
        elif debt == 0:
            debt_free_count += 1
    
    print(f"Customers with debt over ${debt_limit:.0f}: {over_limit_count}")
    print(f"Customers debt free: {debt_free_count}")
    
    # Step 5: Process state-specific data
    # Filter customers who live in the specified state
    state_names = []
    state_debts = []

    for i in range(num_customers):  # Only consider the specified number of customers
        if states[i] == state_abbr:
            state_names.append(names[i])
            state_debts.append(debts[i])

    # Output the state-specific report
    print(f"\n{state_abbr} Report")
    print(f"Customers: {len(state_names)}")
    
    # Find highest debt in the state
    highest_debt_state = -1
    highest_debt_name_state = ""
    for i in range(len(state_names)):
        if state_debts[i] > highest_debt_state:
            highest_debt_state = state_debts[i]
            highest_debt_name_state = state_names[i]
    
    print(f"Highest debt: {highest_debt_name_state}")
    
    # Count customer names that start with the search phrase in this state
    state_search_count = 0
    for name in state_names:
        if name.startswith(search_phrase):
            state_search_count += 1
    
    print(f"Customer names that start with \"{search_phrase}\": {state_search_count}")
    
    # Count customers with debt over the limit and debt-free customers in this state
    state_over_limit_count = 0
    state_debt_free_count = 0
    for debt in state_debts:
        if debt > debt_limit:
            state_over_limit_count += 1
        elif debt == 0:
            state_debt_free_count += 1
    
    print(f"Customers with debt over ${debt_limit:.0f}: {state_over_limit_count}")
    print(f"Customers debt free: {state_debt_free_count}")
