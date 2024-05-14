'''Write a program to create a dictionary containing the author name as the keys and
ISBN number as the value. Make up the data for five dictionary entries and
demonstrate the use of clear() and fromkeys() method.'''

def main():
    # Creating a dictionary with author names as keys and ISBN numbers as values
    author_isbn_dict = {
        "Author1": "ISBN1",
        "Author2": "ISBN2",
        "Author3": "ISBN3",
        "Author4": "ISBN4",
        "Author5": "ISBN5"
    }

    # Displaying the original dictionary
    print("Original Dictionary:")
    print(author_isbn_dict)

    # Demonstrate the clear() method
    author_isbn_dict.clear()
    print("\nAfter clearing the dictionary:")
    print(author_isbn_dict)

    # Create a new dictionary with the same keys using fromkeys() method
    keys = ["Author1", "Author2", "Author3", "Author4", "Author5"]
    new_dict = dict.fromkeys(keys, "Unknown")
    print("\nNew dictionary created using fromkeys() method:")
    print(new_dict)

if __name__ == "__main__":
    main()
