def str_change(userstr):
    userstr = userstr.replace(" ", "").lower()
    if userstr == userstr[::-1]:
        return True
    else:
        return False

userstr = str(input())

if str_change(userstr) == True:
    print(userstr, "is a palindrome")
elif str_change(userstr) == False:
    print(userstr, "is not a palindrome")
