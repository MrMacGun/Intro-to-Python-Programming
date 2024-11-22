#Program takes a password and modifies it
#Guess is that algorithm takes each ACII character in the string and subtracts by a different number
word = input()
password = ''
i = 0

while i < len(word):
    if word[i]=='i':
       password +='1'
    elif word[i]=='a':
       password +='@'
    elif word[i]=='m':
       password +='M'
    elif word[i]=='B':
       password +='8'
    elif word[i]=='s':
       password +='$'
    else:
        password += word[i]
    i +=1
password = password + '!'
print(password)
