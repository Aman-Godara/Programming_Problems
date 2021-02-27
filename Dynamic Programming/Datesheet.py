"""N exams numbered from 1 to N are going be held at Geekland state university.
Geek is a renowned professor at the university and therefore is given the task to design the datesheet for exams.
Datesheet must be made in such a way that total number of holidays in the datesheet is exactly K i.e. sum of holidays given for each exam is exactly K.
Moreover, no exam should have more than M holidays and every exam should have atleast 1 holiday.
Two datesheets are considered different if number of holidays for any exam in the two datesheets is different.
Find number of possible valid datesheets Geek can choose from.

Example 1:

Input:
N = 2
K = 3
M = 2
Output:
2
Explanation:
There are two options:
1. 1 holiday in 1st exam and 2 holidays 
   in 2nd exam.
2. 2 holidays in 1st exam and 1 holiday
   in 1st exam.
Your Task:
Complete the function datesheet() which takes the number of exams N, total number of holidays K and integer M as input parameters and returns the number of valid datesheets.

Expected Time Complexity: O(N * K)
Expected Auxiliary Space: O(N * K)"""


def datesheet(n: int, k: int, m: int):
    if n > 0 and k > 0 and m > 0:
        dp = []
        for i in range(0, k):
            if i + 1 > m:
                temp = [0] + [0] * (n - 1)
                dp.append(temp)
            else:
                temp = [1] + [0] * (n - 1)
                dp.append(temp)

        for i in range(1, k):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                if i - m - 1 >= 0:
                    dp[i][j] -= dp[i - m - 1][j - 1]
        return dp[k - 1][n - 1]
    return -1
  
  # Driver Code
  print(datesheet(5, 24, 7))
