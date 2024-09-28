# 10.7 LAB: Count characters
# Write a program whose input is a string which contains a character and a phrase, 
# and whose output indicates the number of times the character appears in the phrase
# The output should include the input character and use the plural form, n's, 
# if the number of times the characters appears is not exactly 1.

user_char = str(input())

Lchar = user_char[0]
Schar = user_char[2:]

LcharN = Schar.count(Lchar)

if LcharN == 1:
    print(f"{LcharN} {Lchar}")

else:
    print(f"{LcharN} {Lchar}'s")