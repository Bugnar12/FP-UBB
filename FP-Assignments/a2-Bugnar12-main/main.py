import random
"""
First of all I will define a couple functions for facilization of the program,
and afterwards I will implement the two sorting methods I selected that being : 
Insertion sort and shell sort.
"""

#insertion sort : it is the method where we choose elements two by two and we check if the one on the
#right is bigger than the one from the left, and swap them if so.

#the parameters of the function are the array of the list to be sorted and the variable step

def insert_sort(arr, step):
    step = 0
    for i in range(1, len(arr)):
        key = arr[i] #we check if the elements 0...i-1 are greater than the key, and move them one position ahead
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            step += 1
            if step == step1:
                print("This is the array after the given number of steps(I) :", arr)
                step = 0
        arr[j + 1] = key

#shell sort basically takes a distance between 2 elements and swaps the elements from the beginning
#of the distance to that which is at the end of it until it reaches the final element
#afterwards we reduce the gap/2

def shell_sort(arr, step):
    step = 0
    n = len(arr)
    dif = n // 2
    while dif > 0:
        for i in range(dif, n):
            aux = arr[i]
            j = i
            while j >= dif and arr[j-dif] > aux:
                step += 1
                arr[j] = arr[j - dif]
                j -= dif
                if step == step2:
                    print("This is the array after the given number of steps(II) :", arr)
                    step = 0
            arr[j] = aux
        dif = dif // 2


#we firstly generate a random list of natural numbers
n = int(input("->"))
list = []
list1 = []
for i in range(n):
    x = random.randint(0, 100)
    list.append(x)
    list1.append(x)


print("The unsorted list is : ", list)
step1 = int(input("how many steps do you want to take for the first sorting?"))
insert_sort(list, step1)
print("The list sorted with the first method is", list)
step2 = int(input("how many steps do you want to take for the second sorting?"))
shell_sort(list1, step2)
print("The list sorted with the second method is", list1)


