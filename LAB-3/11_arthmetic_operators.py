def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def floordivision(num1, num2):
    return num1 // num2

def modulus(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2

num1 = int(input("Enter the First Value  = "))
num2 = int(input("Enter the Second Value = "))

print("The Addition       = ",addition(num1, num2))
print("The Subtraction    = ",subtraction(num1, num2))
print("The Multiplication = ",multiplication(num1, num2))
print("The Division       = ",division(num1, num2))
print("The Floor Division = ",floordivision(num1, num2))
print("The Modulus        = ",modulus(num1, num2))
print("The Exponent       = ",exponent(num1, num2))