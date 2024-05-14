def read_first_n_lines(file_name, n):
    try:
        with open(file_name, "r") as file:
            count = 0
            for line in file:
                print(line.strip())
                count += 1
                if count == n:
                    break
    except FileNotFoundError:
        print("File not found.")

def main():
    file_name = input("Enter the name of the file: ")
    n = int(input("Enter the number of lines to read: "))
    read_first_n_lines(file_name, n)

main()