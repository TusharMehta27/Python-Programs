def largest(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        return num1
    elif(num2>=num1 and num2>=3):
        return num2
    else:
        return num3
    

res=largest(20,10,43)
print(res,"is the greatest")