def discriminant(a, b, c):
    d = b**2 - 4 * a * c
    return d

print("For a quadratic equation in the form of ax^2 + bx + c = 0")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

det = discriminant(a,b,c)

if (det > 0):
    print("The quadratic equation has two real roots.")
elif (det == 0):    
    print("The quadratic equation has one real root.")
else:
    print("The quadratic equation doesn't have any real root.")