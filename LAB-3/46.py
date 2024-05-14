'''Write a program that has the dictionary of your friends’ names as keys and phone
numbers as its values. Print the dictionary in a sorted order. Prompt the user to
enter the name and check if it is present in the dictionary. If the name is not
present, then enter the details in the dictionary.'''

def print_sorted_dictionary(phone_book):
    sorted_phone_book = sorted(phone_book.items())
    print("Phone Book (Sorted by Names):")
    for name, phone_number in sorted_phone_book:
        print(f"{name}: {phone_number}")

def main():
    # Initialize the phone book dictionary
    phone_book = {
        "Alice": "1234567890",
        "Bob": "9876543210",
        "Charlie": "4567890123"
    }

    # Print the sorted phone book
    print_sorted_dictionary(phone_book)

    # Prompt the user to enter a name
    name = input("\nEnter a name to check if it's present in the phone book: ")

    # Check if the name is present in the phone book
    if name in phone_book:
        print(f"{name} is present in the phone book.")
    else:
        # If the name is not present, prompt the user to enter details
        phone_number = input("Enter the phone number for this name: ")
        phone_book[name] = phone_number
        print("Details added to the phone book.")

    # Print the updated phone book
    print("\nUpdated Phone Book:")
    print_sorted_dictionary(phone_book)

if __name__ == "__main__":
    main()
