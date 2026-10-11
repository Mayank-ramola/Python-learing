# write a program to salary as input using conditional statements to calculate the final tax rate.

salary = input("Enter your salary: ")
salary = float(salary)
if salary < 30000:
    print("Salary after 5% tax is : ", salary - (salary * 0.05))
elif salary >= 30000 and salary <= 70000:
    print("Salary after 15% tax is : ", salary - (salary * 0.15))
else:
    print("Salary after 25% tax is : ", salary - (salary * 0.25))