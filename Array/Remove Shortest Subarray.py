"""Given an array arr[] consisting of N integers, the task is to print the length of the smallest subarray (a contiguous subset array of arr[])
to be removed from arr[] such that the remaining array is non-decreasingly sorted"""


def findShortestSubarrayLength(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer and arr[left_pointer] <= arr[left_pointer + 1]:
        left_pointer = left_pointer + 1
    
    while left_pointer < right_pointer and arr[right_pointer - 1] <= arr[right_pointer]:
        right_pointer = right_pointer - 1

    if left_pointer < right_pointer:
        # left_pointer hasn't crossed right_pointer
        answer = len(arr)
        current = float('-inf')
        for i in range(-1, left_pointer + 1):
            # for every i in set {-1, ....., left_pointer} we are calculating the best possible value of right_pointer
            while right_pointer < len(arr) and current > arr[right_pointer]:
                right_pointer += 1
            # right_pointer - 1 - i: number of indexes in set {i + 1, ........., right_pointer - 1}
            answer = min(answer, right_pointer - 1 - i)
            current = arr[i + 1]
        return answer
    else:
        # left_pointer crossed right_pointer: input array is already non-decreasingly sorted
        return 0

# Driver Code from here
arr1 = [1, 2, 3, 10, 4, 2, 3, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 2, 3]
arr4 = [10, 9, 8, 7, 5, 6, 7, 8, 9]
arr5 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
arr6 = [5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9]

print(findShortestSubarrayLength(arr6))
