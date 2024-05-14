sum=0
n=int(input("Enter the series limit :"))
for i in range (1,n+1):
    sum=sum+pow(i,i)/i
    
print(sum)

