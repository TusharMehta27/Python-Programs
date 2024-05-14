def gender_checker(name,gender):

    if (gender=="M" or gender=="m"):
         return"Hello, Mr."+name
    elif (gender=="F" or gender == "f"):
       return"Hello, Ms."+name
    else:
        return "Please enter only M or F in gender"


name=input("Enter your name : ")
gender=input("Enter your Gender (M for Male and F for Female): ")

res=gender_checker(name,gender)
print(res)


