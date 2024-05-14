'''Write a program to create an intersection, union, set difference, and symmetric
difference of sets.'''

def main():
    set1 = {5,8,6,2,7}
    set2 = {3,9,4,2,1}

    # Intersection
    intersection_set = set1.intersection(set2)
    print("Intersection:", intersection_set)

    # Union
    union_set = set1.union(set2)
    print("Union:", union_set)

    # Set difference
    difference_set = set1.difference(set2)
    print("Set Difference (set1 - set2):", difference_set)

    # Symmetric difference
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Symmetric Difference:", symmetric_difference_set)

if __name__ == "__main__":
    main()
