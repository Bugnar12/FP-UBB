import random

import time


"""
So we have the sorting algorithms implemented, and we need to analyze the complexity.

*NOTE* -> insertion sort is best for small lists, whilst for lists with greater number of
variables it is not so efficient.

For insertion sort it is : 
1.Worst case = O(n^2) -> the array is in reverse order
2.Average case = O(n^2)
3.Best case = O(n) -> linear ; we encounter this time complexity when the list is already sorted and is went over
only once.
4.Space complexity : O(1) -> constant ; which means there is no extra space needed for the sorting, only the list we
have to call from outside the function
"""

#insertion sort : it is the method where we choose elements two by two and we check if the one on the
#right is bigger than the one from the left, and swap them if so.


def insert_sort(arr):
    for i in range(1, len(arr)): #O(n)
        key = arr[i] #we check if the elements 0...i-1 are greater than the key, and move them one position ahead
        j = i - 1
        while j >= 0 and key < arr[j]: #possible O(n) if the array is not sorted or almost sorted
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#shell sort basically takes a distance between 2 elements and swaps the elements from the beginning
#of the distance to that which is at the end of it until it reaches the final element
#afterwards we reduce the gap/2

"""
Description : Shellsort is an optimization of insertion sort that allows the exchange of items that are far apart,
and is better used for larger data structures.

Time complexion analysis of shell-sort:
1.Worst case : O(n^2) ->if the array is sorted in reverse
2.Average case : O(n * log n) -> the degree complexity is determined by the size of the interval
3.Best case : O(n * log n) -> the array is already sorted
4.Space complexity : O(1) -> linear
"""

def shell_sort(arr): # 12 34 54 2 3 gap = 1
                     # 0  1  2  3 4
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):  # O(n)
            aux = arr[i]
            j = i
            while j >= gap and arr[j-gap] > aux: #O(logn)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = aux
        gap = gap // 2



#we firstly generate a random list of natural numbers
n = int(input("Press the following key for showing: \n 1 -> Best case \n 2 -> Average case \n 3 -> Worst case \n ->"))

#we generate five lists with random elements
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
for i in range (0,999):
    x = random.randint(1, 1000000)
    list1.append(x)

for i in range (0, 1999):
    x = random.randint(1, 1000000)
    list2.append(x)

for i in range (0, 3999):
    x = random.randint(1, 1000000)
    list3.append(x)

for i in range (0,7999):
    x = random.randint(1, 1000000)
    list4.append(x)

for i in range (0,15999):
     x = random.randint(1, 1000000)
     list5.append(x)

"""
The five lists will be sorted and then we will use time() to measure the time it takes to execute
each sorting algorithm
"""
if n == 1: #this is the best case so the list is already sorted

    list1.sort()
    list2.sort()
    list3.sort()
    list4.sort()
    list5.sort()

    print("For insertion sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print (end_time - start_time , "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print (end_time - start_time , "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print (end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print (end_time - start_time , "fifth test -> 16000 variables \n")

    print("For shell sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print(end_time - start_time, "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print(end_time - start_time, "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print(end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print(end_time - start_time, "fifth test -> 16000 variables \n")

"""
The five lists will be ordered randomly, anyways the average case is not the most accurate 
to be determined in neither of the cases.
"""

if n == 2: #this is the average case so I will consider taking elements randomly

    print("For insertion sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print(end_time - start_time, "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print(end_time - start_time, "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print(end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print(end_time - start_time, "fifth test -> 16000 variables \n")

    print("For shell sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print(end_time - start_time, "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print(end_time - start_time, "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print(end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print(end_time - start_time, "fifth test -> 16000 variables \n")

"""
In the worst case the lists will be ordered in reverse, and in both the sorting algorithms this way 
will take the most number of steps.
"""
if n == 3: #this is the worst case so in both variants the list will be sorted backwards

    list1.sort(reverse=True)
    list2.sort(reverse=True)
    list3.sort(reverse=True)
    list4.sort(reverse=True)
    list5.sort(reverse=True)

    print("For insertion sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print(end_time - start_time, "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print(end_time - start_time, "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print(end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print(end_time - start_time, "fifth test -> 16000 variables \n")

    print("For shell sort we have the following tests : \n")

    start_time = time.time()
    insert_sort(list1)
    end_time = time.time()
    print(end_time - start_time, "first test -> 1000 variables")

    start_time = time.time()
    insert_sort(list2)
    end_time = time.time()
    print(end_time - start_time, "second test -> 2000 variables")

    start_time = time.time()
    insert_sort(list3)
    end_time = time.time()
    print(end_time - start_time, "third test -> 4000 variables")

    start_time = time.time()
    insert_sort(list4)
    end_time = time.time()
    print(end_time - start_time, "fourth test -> 8000 variables")

    start_time = time.time()
    insert_sort(list5)
    end_time = time.time()
    print(end_time - start_time, "fifth test -> 16000 variables \n")
