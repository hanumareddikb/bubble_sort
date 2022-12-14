"""This project sorts the given array in the increasing order using Bubble sort algorithm"""

# function for sorting the array
def bubbleSort(arr):  
    swapped = False
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i] > arr[i + 1]:  # indicates sorting is needed
                swapped = True  
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if not swapped:  # if array is already sorted 
            return

arr1 = [2,4,1,5,3]
bubbleSort(arr1)
print(arr1)
