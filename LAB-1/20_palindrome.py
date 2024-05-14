n=int(input("Enter the number : "))
rev=0
temp=n

while temp > 0:
    digit = (temp % 10)
    rev = (rev * 10) + digit
    temp = temp // 10

if(n == rev):
    print("The entered number is a palindrome.")
else:
    print("The entered number is not a palindrome.")