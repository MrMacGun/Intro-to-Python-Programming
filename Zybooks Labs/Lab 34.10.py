#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/10
#Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange
#followed by an equivalent number of string inputs representing the stock selections
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

total = 0.0
userint = int(input())

for i in range(userint):
    stockinput = str(input())
    total = stocks[stockinput] + total

print(f'Total price: ${total:.2f}')