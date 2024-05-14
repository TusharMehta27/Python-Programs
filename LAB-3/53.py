'''Write a program to add two polynomials using classes.'''

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs[::-1]  # Reverse the coefficients for easier manipulation

    def add(self, other):
        # Pad the coefficients of the shorter polynomial with zeros
        if len(self.coeffs) < len(other.coeffs):
            self.coeffs.extend([0] * (len(other.coeffs) - len(self.coeffs)))
        elif len(other.coeffs) < len(self.coeffs):
            other.coeffs.extend([0] * (len(self.coeffs) - len(other.coeffs)))
        
        # Add corresponding coefficients
        result_coeffs = [a + b for a, b in zip(self.coeffs, other.coeffs)]

        return Polynomial(result_coeffs[::-1])  # Reverse the result to get the correct order of coefficients

    def __str__(self):
        terms = []
        for power, coeff in enumerate(self.coeffs[::-1]):
            if coeff != 0:
                term = f"{coeff}x^{power}" if power > 1 else (f"{coeff}x" if power == 1 else str(coeff))
                terms.append(term)
        return " + ".join(terms) if terms else "0"

# Example usage:
if __name__ == "__main__":
    # Define two polynomials
    poly1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
    poly2 = Polynomial([4, 5, 6])  # 6x^2 + 5x + 4

    # Add the polynomials
    result_poly = poly1.add(poly2)

    # Display the result
    print("Polynomial 1:", poly1)
    print("Polynomial 2:", poly2)
    print("Sum:", result_poly)
