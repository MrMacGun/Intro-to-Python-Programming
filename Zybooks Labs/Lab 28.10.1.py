#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/10

uint = input()

new_list = list(map(int, uint.split(" ")))
min2 = []

for i in new_list:
    min_var1 = min(new_list)
    if i != min_var1:
        min2.append(i)

min_var2 = min(min2)

print(min_var1,"and",min_var2)