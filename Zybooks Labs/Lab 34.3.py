#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/3
#Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

userint = int(input())

element = various_data_types[userint]
print(f"Element {userint}: {type(element).__name__}")