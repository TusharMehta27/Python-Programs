'''Write a program to Add a list of elements to a set.'''

my_set = {"apple", "banana", "cherry"}

elements_to_add = ["banana", "kiwi", "mango", "apple", "orange"]

for element in elements_to_add:
    my_set.add(element)

print("Updated set:", my_set)
