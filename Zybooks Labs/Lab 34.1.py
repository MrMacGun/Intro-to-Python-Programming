#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/34/section/1
#Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site
# Output the total distance traveled to two decimal places given the following miles per employee commute to the job site.

employeeA = 15.62
employeeB = 41.85
employeeC = 32.67

userintA = employeeA * (int(input()))
userintB = employeeB * (int(input()))
userintC = employeeC * (int(input()))

total = userintA + userintB + userintC

print(f'Distance: {total:.2f} miles')