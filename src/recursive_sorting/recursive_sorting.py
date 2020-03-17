# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO

    merged_arr = []

    A = 0
    B = 0
    while A < len(arrA) and B < len(arrB):
        if arrA[A] < arrB[B]:
            merged_arr.append(arrA[A])
            A += 1
        else:
            merged_arr.append(arrB[B])
            B += 1

    merged_arr.extend(arrA[A:])
    merged_arr.extend(arrB[B:])

    
    return merged_arr


# implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        return merge(merge_sort(arr[0:mid]), merge_sort(arr[mid:len(arr)]))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
