"""Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears
after the smaller number."""


def best_time_stocks(arr):
    if len(arr) > 0:
        best_selling_price = (0, 0, 0)
        minimum_price_so_far_index = 0
        for i in range(1, len(arr)):
            todays_price = arr[i]
            if todays_price < arr[minimum_price_so_far_index]:
                minimum_price_so_far_index = i
            else:
                todays_profit = todays_price - arr[minimum_price_so_far_index]
                if todays_profit > best_selling_price[0]:
                    best_selling_price = (todays_profit, minimum_price_so_far_index, i)
        return best_selling_price


arr1 = [5, 6, 7, 8, 7.8, 6.4, 8.2, 9, 10, 11, 12, 11.5, 10, 8.9, 7.6, 6, 5, 4, 3, 1]
print(best_time_stocks(arr1))

"""The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all."""


def stocks(arr):
    if len(arr) > 0:
        answer_arr = []
        buy_price_index = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[buy_price_index]:
                buy_price_index = i
            else:
                if i == len(arr) - 1 or arr[i] >= arr[i + 1]:
                    # using arr[i] > (not >=) arr[i + 1] will give same results but in different format, see example [12, 59, 5, 9, 29, 29, 99]
                    profit = arr[i] - arr[buy_price_index]
                    answer_arr.append((profit, buy_price_index, i))
                    buy_price_index = i
        return answer_arr


arr2 = [100, 180, 260, 310, 40, 535, 695]
arr3 = [12, 59, 5, 9, 29, 29, 99]
print(stocks(arr3))
