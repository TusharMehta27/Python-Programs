Year=int(input("Enrter the year : "))

if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
    print(f"{Year} is a leap Year")
else:  
    print (f"{Year} is not a leap Year")  