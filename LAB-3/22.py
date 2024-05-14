'''Write a program to sort the elements in ascending order using insertion sort.'''

def insertion_sort(num):
    for i in range(1,len(num)):
        key=num[i]

        j=i-1
        while j>=0 and key<num[j]:
            num[j+1]=num[j]
            j=j-1
        num[j+1]=key

num=[10,50,28,6,4]
print("The original list : ",num)

insertion_sort(num)
print("The sorted list : ",num)
