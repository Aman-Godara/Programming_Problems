"""Geek is a spy in an enemy town.
There are N people in the town and every person has a unique natural number that denotes their identification.
The ith person's identification code is i. His organisation has however, planted several allies in the town.
They can be identified by their identification code as the digits in their codes form the smallest possible permutation.
Given N, find out how many allies Geek has in the town.

Example 1:
Input: N = 13
Output: 12
Explanation: Identification codes of Geek's allies are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12 and 13.
Person with Identification code 10 cannot be an ally as 10 is not the smallest permutation of the digits '0' and '1'."""


def ally(n: int):
    digits = str(n)
    length = len(digits)
    dp = [None] * length
    calculate_from = [9] * length
    for i in range(length):
        dp[i] = [None] * 10

    def allies(current_index: int, start: int, equal: bool):
        if current_index == length:
            return 1
        end = int(digits[current_index])
        next_sum = 0
        if not equal:
            end = calculate_from[current_index]
            if end < start:
                return dp[current_index][start]
            next_sum = dp[current_index][end + 1] if end < 9 else 0
            calculate_from[current_index] = start - 1
        for j in range(end, start - 1, -1):
            next_sum += allies(current_index + 1, j, equal and j == end)
            dp[current_index][j] = next_sum
        return next_sum

    return allies(0, 0, True) - 1

# Driver Code
print(ally(500**8))
