from math import factorial
rows=int(input("Enter the rows : "))

for n in range(rows):
    for space in range(rows-n+1):
        print(end=' ')
    for r in range(n+1):
        ncr=factorial(n)//(factorial(r) * factorial(n-r))
        print(ncr,end=" ")

    print(" ")