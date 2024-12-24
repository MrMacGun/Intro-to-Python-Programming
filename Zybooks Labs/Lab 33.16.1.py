#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/33/section/16
#Write a program to calculate the total price for car wash services
#A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. 
#Two additional services can be selected. A '-' signifies an additional service was not selected.
#Output all selected services, according to the input order, along with the corresponding costs and then the total price for all car wash services.

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

print("ZyCar Wash")
print("Base car wash -- $10")
total = 10  

if service_choice1 in services:
    new_service_choice1 = services[service_choice1]
    total += new_service_choice1 
    print(f'{service_choice1} -- ${new_service_choice1}')

if service_choice2 in services:
    new_service_choice2 = services[service_choice2]
    total += new_service_choice2
    print(f'{service_choice2} -- ${new_service_choice2}')

print("----")
print(f'Total price: ${total}')

