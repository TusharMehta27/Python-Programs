name=input("Enter student name:")
roll_no=int(input("Enter the roll number: "))

m1=int(input("Enter english marks:"))
m2=int(input("Enter hindi marks:"))
m3=int(input("Enter maths marks:"))
m4=int(input("Enter computer marks:"))

total_marks=m1+m2+m3+m4
per=total_marks/4

print("Total marks:",total_marks)
print("Percentage",per)

if(per>=90):
    grade="A"
elif(per<90 and per>=80):
    grade="B"
elif(per<80 and per>=70):
    grade="C"
elif(per<70 and per>=60):
    grade="D"
else:
    grade="E"

print("Your Overall Grade is :",grade)