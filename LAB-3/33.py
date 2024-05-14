'''Write a program that reads the contents of the file and counts the occurrences of
each letter. Prompt the user to enter the filename.'''

def occurrences(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read().lower()
            letter_count = {}
            for char in content:
                if char.isalpha():
                    letter_count[char] = letter_count.get(char, 0) + 1
            return letter_count
    except FileNotFoundError:
        print("File not found.")
        return {}

def main():
    file_name = input("Enter the filename: ")
    letter_count = occurrences(file_name)
    if letter_count:
        print("Letter occurrences in the file:")
        for letter, count in sorted(letter_count.items()):
            print(f"{letter}: {count}")

if __name__ == "__main__":
    main()
