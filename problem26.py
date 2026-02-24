employees = eval(input("Enter dictionary: "))
max=0
max_employee=""
for key,value in employees.items():
    if value >max:
        max=value
        max_employee=key
print("Highest Salary Employee: ",max_employee)
print("Salary",max)
