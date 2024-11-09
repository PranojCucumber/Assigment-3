import random

def partition_randomized(arr, low, high):
    # random pivot index is being selected between high and low
    idx_pivot = random.randint(low, high)
    # moving the pivot element to the end of the array
    arr[idx_pivot], arr[high] = arr[high], arr[idx_pivot]
    ele_pivot = arr[high]
    i = low - 1

    # making partitions of the array
    for j in range(low, high):
        if arr[j] < ele_pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # replace the pivot element into the right place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_randomized(arr, low, high):
    if low < high:
        # making partition around pivot element and storing its index
        idx_pivot = partition_randomized(arr, low, high)
        # sort elements before and after partition recursively
        quicksort_randomized(arr, low, idx_pivot - 1)
        quicksort_randomized(arr, idx_pivot + 1, high)

def quicksort(arr):
    # check if array is empty or with one element
    if len(arr) <= 1:
        return arr
    quicksort_randomized(arr, 0, len(arr) - 1)
    return arr

# Test cases
arr1 = [2, 6, 2, 5, 4, 9, 5, 1]   # General case: with repeated elements
arr2 = []                         # Edge case: empty array
arr3 = [4, 4, 4, 4, 4]            # Edge case: all elements are the same
arr4 = [1, 2, 3, 4, 5]            # Edge case: already sorted array
arr5 = [5, 4, 3, 2, 1]            # Edge case: reverse sorted array

# Testing the function
print("Sorted arr1:", quicksort(arr1))
print("Sorted arr2:", quicksort(arr2))
print("Sorted arr3:", quicksort(arr3))
print("Sorted arr4:", quicksort(arr4))
print("Sorted arr5:", quicksort(arr5))
