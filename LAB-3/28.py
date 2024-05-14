my_tuple = (1, 2, 3, 4, 5)

item_to_check = int(input("Enter the Number to find :"))

if item_to_check in my_tuple:
    print(f"{item_to_check} exists in the tuple.")
else:
    print(f"{item_to_check} does not exist in the tuple.")
