""" Find the smallest missing positive integer from an unsorted array of integers
Input: [-1, 0, 3, 2, 3, 4, 1, 6]
Output: 5 """


def minPostiveNumber(arr):
    length = len(arr)
    for i in range(len(arr)):
        correct_pos = arr[i] - 1
        while 0 <= correct_pos < length and arr[correct_pos] - 1 != correct_pos:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            correct_pos = arr[i] - 1

    for i in range(length):
        if arr[i] - 1 != i:
            return i + 1
    return length + 1


print(minPostiveNumber([-1, 0, 3, 2, 3, 4, 1, 6]))
