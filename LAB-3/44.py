'''Write a Python program to find the highest 2 values in a dictionary.'''

def find_highest_2_values(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    highest_2_values = sorted_values[:2]
    return highest_2_values

def main():
    my_dict = {'a': 30, 'b': 20, 'c': 10, 'd': 50, 'e': 60 ,'f':40}

    highest_2_values = find_highest_2_values(my_dict)

    print("Highest 2 values in the dictionary:", highest_2_values)

if __name__ == "__main__":
    main()
