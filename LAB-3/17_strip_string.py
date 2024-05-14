str = input("Enter a string : ")
strip_char = input("Enter Set of Characters : ")

new_str=""
for i in str:
    if i not in strip_char:
        new_str+=i

print(f"Resulting String is :{new_str}")