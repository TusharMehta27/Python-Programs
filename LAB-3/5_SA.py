# Function to calculate the surface area of a rectangular prism
def calculate_surface_area(a, b, c):
    surface_area = 2 * (a * b + b * c + c * a)
    return surface_area

# Main function to get inputs and print the surface area
def main():
    # Taking inputs
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    
    # Calculating surface area
    surface_area = calculate_surface_area(a, b, c)
    
    # Printing the result
    print("The surface area of the prism is:", surface_area)

# Calling the main function
if __name__ == "__main__":
    main()
