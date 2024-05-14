str= input("Enter a String : ")
N=int(input("Enter The Value of N : "))

if N<0:
    print("Value of N is Invalid ")
else:
    print(f"the first {N} characters of a string ")
    new_str=str[:N]
    print(new_str)