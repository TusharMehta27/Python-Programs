'''Describe with an example how to read and write to a text file.'''

# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, My Name is Tushar Mehta.\n")
    file.write("Im a student of Jain University.\n")


# Reading from a text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)
