def compound_int(p,r,t,n=1):
    amount=p*(1+r/(n*100))**(n*t)
    ci = round(amount - p, 2)
    return ci

p=int(input("Enter the Principle Amount : "))
r=float(input("Enter the Interest rate : "))
t = float(input("Enter total time: "))
n = int(input("Number of times the interest is compounded in a year : "))


res=compound_int(p,r,t,n)
print(res)