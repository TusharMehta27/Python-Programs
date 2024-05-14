#Program to input five numbers and print largest and smallest numbers
min  = 0
max = 0
for a in range(0,5):
    x = int(input("Enter the number: "))
    if a == 0:
        min =x
        max =x
    if(x < min):
        min = x
    if(x > max):
        max = x
print("The Minimum number is",min)
print("The Maximum number is ",max)