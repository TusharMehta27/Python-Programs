#Program to check the eligibility for driving license
name = input("What is your name? ")
age = int(input("What is your age? "))

#Checking the age and displaying the message accordingly

if(age>=18):
    print("You are eligible to apply for the driving license.")
else:
    print("You are not eligible to apply for the driving license.")