def kadanes_algo(input_list):
    max_sum_indexes = (-1, -1)
    max_sum = 0  # float('-inf'): use "-inf" here if you want to have atleast 1 element in the required output contiguous subarray
    max_sum_with_ith_indexes = (-1, -1)
    max_sum_with_ith = float('-inf')  # max_sum_with_ith can be assigned any value less than or equal to 0 (<= 0)
    for i in range(len(input_list)):
        max_sum_with_ith = max(max_sum_with_ith + input_list[i], input_list[i])
        if max_sum_with_ith == input_list[i]:
            max_sum_with_ith_indexes = (i - 1, i)
        else:
            max_sum_with_ith_indexes = (max_sum_with_ith_indexes[0], i)
        if max_sum_with_ith > max_sum:
            max_sum = max_sum_with_ith
            max_sum_indexes = max_sum_with_ith_indexes
    print("maximum sum: (from this index exclusive, to this index inclusive]")
    return str(max_sum) + ': ' + '(' + str(max_sum_indexes[0]) + ', ' + str(max_sum_indexes[1]) + ']'


print(kadanes_algo([-4, -2, -3, -4, -5]))
