'''Create a class named quadratic, where a, b, c are data attributes and the methods
are
a. __init__() to initialize the data attributes
b. roots() to compute the quadratic equation'''

import math

class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def roots(self):
        discriminant = self.b**2 - 4 * self.a * self.c
        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return root
        else:
            return "Complex roots"

# Example usage:
if __name__ == "__main__":
    a = float(input("Enter the coefficient of x^2 (a): "))
    b = float(input("Enter the coefficient of x (b): "))
    c = float(input("Enter the constant term (c): "))

    equation = quadratic(a, b, c)
    roots = equation.roots()
    print("Roots of the quadratic equation:", roots)
