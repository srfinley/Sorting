# Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]




    return arr


# implement the Bubble Sort function below
def bubble_sort( arr ):
    for _ in range(len(arr)):
        count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    minimum = 0
    for _, value in enumerate(arr):
        if value < minimum:
            return "Error, negative numbers not allowed in Count Sort"
        if value > maximum:
            maximum = value

    count = [0 for _ in range(maximum+1)]

    for value in arr:
        count[value] += 1
    
    arr = []
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr