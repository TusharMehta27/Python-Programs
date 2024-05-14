'''Create a class called library with data attributes like acc_number, publisher, title and
author. The methods of the class should include
a. read() acc_number, title, author.
b. compute() - to accept the number of days late, calculate and display the fine
charged at the rate of Rs 15 per day.
c. display the data.'''

class Library:
    def __init__(self, acc_number, publisher, title, author):
        self.acc_number = acc_number
        self.publisher = publisher
        self.title = title
        self.author = author
        self.days_late = 0
    
    def read(self):
        print("Enter Library Details:")
        self.acc_number = input("Accession Number: ")
        self.title = input("Title: ")
        self.author = input("Author: ")

    def compute(self):
        self.days_late = int(input("Enter the number of days late: "))
        fine = self.days_late * 15
        print(f"Fine charged: Rs {fine}")

    def display(self):
        print("\nLibrary Details:")
        print("Accession Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)
        if self.days_late > 0:
            print("Days Late:", self.days_late)

# Example usage:
if __name__ == "__main__":
    library_book = Library("", "", "", "")
    library_book.read()
    library_book.compute()
    library_book.display()
