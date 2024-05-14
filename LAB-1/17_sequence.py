num = int(input("Enter the number: "))
for a in range(1,num+1): 
    if(a%2 == 0): 
        print(a * 5, end=",") 
    else: 
        print(a * 5 * (-1),end=",")
