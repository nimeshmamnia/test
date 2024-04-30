''' You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0'''


def coin_change(coins, amount):
    n = len(coins)
    # Create a DP table with (n+1) rows for each coin plus an extra for zero-coin scenario,
    # and (amount+1) columns for each amount from 0 to amount
    t = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

    # Set the first column to 0, because 0 amount requires 0 coins
    for i in range(n + 1):
        t[i][0] = 0

    # Initialize the first row for amounts that are not zero; these are inf since no amount > 0 can be formed with 0
    # coins
    for j in range(1, amount + 1):
        t[0][j] = float('inf')

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                # Include the coin: add one coin to the number of coins needed to make up the amount j - coin value
                t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]])
            else:
                # Exclude the coin: take the value from the previous row (same amount, without this coin)
                t[i][j] = t[i - 1][j]

    # The bottom-right cell of the matrix will hold the answer
    return t[n][amount] if t[n][amount] != float('inf') else -1


# Example usage
coins1 = [1, 2, 5]
amount1 = 11
print("Minimum number of coins to get the amount:", coin_change(coins1, amount1))

coins2 = [2]
amount2 = 3
print("Minimum number of coins to get the amount:", coin_change(coins2, amount2))

coins3 = [1]
amount3 = 0
print("Minimum number of coins to get the amount:", coin_change(coins3, amount3))
