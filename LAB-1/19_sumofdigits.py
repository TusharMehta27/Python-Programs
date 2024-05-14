n=int(input("Enter the digit : "))
sum=0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n//10

print("The sum of digits of the number is",sum)
    