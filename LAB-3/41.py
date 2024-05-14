'''Write a program to Check if two sets have any elements in common. If yes, display
the common elements'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

ce=set1.intersection(set2)

print("The common elements are: " , ce)
