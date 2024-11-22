#User inputs a 9 digit number
#program outputs the numbers a string  with dashes on the first 3 numbers, 2, then 4

userstr = str(input())

userstr1 = userstr[0:3]
userstr2 = userstr[3:5]
userstr3 = userstr[5:9]

print(f'{userstr1}-{userstr2}-{userstr3}')