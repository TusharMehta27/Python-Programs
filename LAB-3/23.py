'''Write a Python program to use binary search to find the key element in the list.'''

def binary_search(num, key):
    low = 0
    high = len(num) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = num[mid]

        if mid_val == key:
            return mid

        elif mid_val < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1

num = [2, 3, 4, 10, 40]
key = 10
result = binary_search(num, key)

if result != -1:
    print("Element", key, "is present at index", result)
else:
    print("Element", key, "is not present in the numay")
