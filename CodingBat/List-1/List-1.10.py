#https://codingbat.com/prob/p171011
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
    slice1 = a[1]
    slice2 = b[1]
    newlist = []
    newlist.append(slice1)
    newlist.append(slice2)
    return newlist
    

print("Enter two list, with the elements seperated via spaces and"
      "list seperated via the enter key. The list will add the middle character")

userint1 = input()
userint2 = input()
userlist1 = list(map(int, userint1.split()))
userlist2 = list(map(int, userint2.split()))

print(middle_way(userlist1, userlist2))