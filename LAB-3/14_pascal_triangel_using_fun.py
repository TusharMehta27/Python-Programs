from math import factorial

def pascal_triangle(rows):

    for n in range(rows):
        for space in range(rows-n+1):
            print(end=' ')
        for r in range(n+1):
            ncr=factorial(n)//(factorial(r) * factorial(n-r))
            print(ncr,end=" ")

        print(" ")

pascal_triangle(5)