sum = 0

n = int(input("Enter the number: "))
for a in range(1,n+1):

    sum = sum + (1/pow(a,3))
    
print("The sum of the series is: ",round(sum,2))