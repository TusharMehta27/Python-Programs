# Define a list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip the list of tuples into individual lists
unzipped_lists = list(zip(*list_of_tuples))

# Print the unzipped lists
for lst in unzipped_lists:
    print(lst)
