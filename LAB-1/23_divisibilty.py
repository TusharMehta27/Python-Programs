# function Defination
def divisibility(n):
    if n % 7==0:
        return "Yes Divisible"
    else:
        return "Not Divisble"
    
#getting the value from user
n=int(input("Enter a Number to check if it is divisible by 7 : "))

#calling the function
res=divisibility(n)
print(res)



