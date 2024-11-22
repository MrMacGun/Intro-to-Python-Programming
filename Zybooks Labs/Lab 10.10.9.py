# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    rate = float(rate)
    print(f'{rate:.2f}')
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)