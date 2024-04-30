""" You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money. Return the number of combinations that make up that amount. If that amount of
money cannot be made up by any combination of the coins, return 0. You may assume that you have an infinite number of
each kind of coin. The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1"""


def coin_change(arr, n, W):
    t = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][W]


coins1 = [1, 2, 5]
amount1 = 5
n1 = len(coins1)
print("Maximum number of ways to get the amount:", coin_change(coins1, n1, amount1))

coins2 = [2]
amount2 = 3
n2 = len(coins2)
print("Maximum number of ways to get the amount:", coin_change(coins2, n2, amount2))

coins3 = [10]
amount3 = 10
n3 = len(coins3)
print("Maximum number of ways to get the amount:", coin_change(coins3, n3, amount3))
