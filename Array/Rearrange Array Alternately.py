"""Given a non-decreasingly sorted array of positive integers, rearrange the array alternately such that
first element is the maximum value, second is the minimum value, third is the second max value, fourth is the second min value and so on.
Input: [1, 2, 3, 4, 5, 6, 7]
Output: [7, 1, 6, 2, 5, 3, 4]"""


def reArrange(arr, print_arr_state=True):
    # arr: non-decreasingly sorted List[positive floats/ints]
    length = len(arr)
    for i in range(length):
        if arr[i] > 0:
            cycler(arr, i, length, print_arr_state)
        arr[i] = abs(arr[i])
        if print_arr_state:
            print('after', i, 'th iteration:', arr)


def cycler(arr, start_index, length, print_cycler_array=True):
    if print_cycler_array:
        print('cycler function:', arr, end=' ---> ')

    half_length_index = length // 2
    swap_index = start_index
    current_value = arr[start_index]
    while True:
        if swap_index < half_length_index:
            swap_index = 2 * swap_index + 1
        else:
            swap_index = 2 * (length - 1 - swap_index)
        swap_value = arr[swap_index]
        arr[swap_index] = -1 * current_value
        current_value = swap_value
        if swap_index == start_index:
            if print_cycler_array:
                print(arr)
            return True


# Driver Code
arr = [12, 23, 28, 43, 44, 59, 60, 68, 70, 85, 88, 92, 124, 125, 136, 168, 171, 173, 179, 199, 212, 230, 277, 282, 306,
       314, 316, 325, 328, 336, 337, 363, 365, 368, 369, 371, 374, 387, 394, 414, 422, 427, 430, 435, 457, 493, 506,
       527, 531, 538, 541, 546, 568, 583, 650, 691, 730, 737, 751, 764, 778, 783, 785, 789, 794, 803, 809, 815, 847,
       858, 863, 874, 887, 896, 916, 920, 926, 927, 930, 957, 981, 997]
reArrange(arr)
print(arr)

"""Please visit https://stackoverflow.com/questions/61206959/rearrange-array-alternately/66075394#66075394 to know more about the algorithm used here."""
