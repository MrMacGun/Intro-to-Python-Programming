names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    if index < -1 * len(names) or index >= len(names):
        # the index error's argument prints inside the except block
        raise IndexError('Exception! list index out of range')
    print(f'Name: {names[index]}')
except IndexError as excpt:
    # selects the closest name to requested index for output
    if index < 0:
        out_str = names[0]
    else:
        out_str = names[len(names)-1]
    # outputs the exception message and the closest name
    print(excpt)
    print(f'The closest name is: {out_str}')