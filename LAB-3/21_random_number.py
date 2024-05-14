import random


# random_numbers = [random.randint(1, 100) for i in range(10)]
# print("Random numbers:", random_numbers)

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

odd_list = []
even_list = []

for num in random_numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Odd numbers:", odd_list)
print("Even numbers:", even_list)

