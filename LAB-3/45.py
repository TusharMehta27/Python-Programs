'''Write a Python program to create a dictionary from a string.'''

def create_dictionary_from_string(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    input_string = input("Enter a string: ")
    dictionary_from_string = create_dictionary_from_string(input_string)
    print("Dictionary from the string:", dictionary_from_string)

if __name__ == "__main__":
    main()
