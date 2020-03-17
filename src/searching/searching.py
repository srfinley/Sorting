# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
    found = -1
    for i, item in enumerate(arr):
        if item == target:
            found = i
            break

    return found   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    middle = (low+high)//2

    while high != low:
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle
            middle = (low+high)//2
        elif arr[middle] < target:
            low = middle
            middle = (low+high)//2

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty YEET

    if len(arr) == 1:
        if arr[0] == target:
            return middle
        else:
            return -1

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle)
    else:
        return binary_search_recursive(arr, target, middle, high)
