"""Faster Implementation of Merge Sort.
I have taken help of a support_array (a shallow copy of the input_array) instead of creating a new array again and again while merging 2 sorted arrays.
This implementation of merge sort takes around half of the time of naive implementation.
The Time Complexity and Space Complexity is still same as to that of the naive implementation"""


def mergeSort(first_array, second_array, i, j):
    if j > i + 1:
        mid = (i + j + 1) // 2
        mergeSort(second_array, first_array, i, mid)
        mergeSort(second_array, first_array, mid, j)
        merge(first_array, second_array, i, mid, j)


def merge(first_array, second_array, i, mid, j):
    left_index, right_index = i, mid
    for k in range(i, j):
        left, right = None, None
        if left_index < mid:
            left = second_array[left_index]
        if right_index < j:
            right = second_array[right_index]
        if secondMustComeBeforeFirst(left, right):
            first_array[k] = right
            right_index += 1
        else:
            first_array[k] = left
            left_index += 1


def secondMustComeBeforeFirst(first, second):
    if second is None:
        return False
    elif first is None:
        return True
    return second < first


def startMergeSort(input_array):
    length = len(input_array)
    support_array = [None] * length
    for i in range(length):
        support_array[i] = input_array[i]
    mergeSort(input_array, support_array, 0, length)
    print(input_array)


# Driver Code
arr1 = [2, 4, 1, 7, 8, 3, 5, 2.9, -1, -0.7, None, 3, 3, 0, 1.3, 2.9, None, 0]
startMergeSort(arr1)
