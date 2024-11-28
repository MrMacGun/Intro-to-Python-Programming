#https://codingbat.com/prob/p147755
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
#Both arrays will be length 1 or more.

def common_end(a, b):
    return a[0] == b[0]

print("Input 2 list of numbers seperated via spaces")
ainput = input()
binput = input()
alist = list(map(int,ainput.split()))
blist = list(map(int,binput.split()))

print("The program will check if the first element is the same in each list")
print(common_end(alist, blist))