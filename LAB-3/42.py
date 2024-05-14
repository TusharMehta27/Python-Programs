'''Write a Python program to input information about a few employees as given below:
a. Name
b. Employee Id
c. Salary'''

n=int(input("Enter number of employes : "))

emp=[]

for i in range(n):
    Name=input("Enter the name of employee : ")
    emp_id=input("Enter employee id : ")
    salary=input("Enter Salary of employee : ")


print("******EMPLOYEE INFORMATION**********")

for i in range(n):
    print("The Name of employee : ",Name)
    print("The employee id of employee : ",emp_id)
    print("The Salary of employee : ",salary)
    