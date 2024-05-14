'''Write a program to Update the first set with items that don’t exist in the second set'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# set1 =set1 - set2
set1.difference_update(set2)

print("Updated first set:", set1)

