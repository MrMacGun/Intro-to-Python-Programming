#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/6
#Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.

phone_number = int(input())
phone_str_slice = str(phone_number)
slice1 = phone_str_slice[0:3]
slice2 = phone_str_slice[3:6]
slice3 = phone_str_slice[6:10]

paren = "(" + slice1 + ")"
adjusted_num = paren + " " + slice2 + '-' + slice3

print(adjusted_num)
