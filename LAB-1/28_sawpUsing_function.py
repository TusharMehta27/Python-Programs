def swap(num1,num2):
    if num1<num2:
        temp=num1
        num1=num2
        num2=temp

        return num1,num2
    elif num1>num2:

        return num1,num2

num1=int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))


num1,num2=swap(num1,num2)

print("The first number is : ",num1)
print("The second NUmber is : ",num2)
