'''Write a program to sort the elements in ascending order using selection sort.'''

def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
                
        num[i], num[min_index] = num[min_index], num[i]

num = [64, 25, 12, 22, 11]
print("Original numay:", num)

selection_sort(num)
print("Sorted numay:", num)
