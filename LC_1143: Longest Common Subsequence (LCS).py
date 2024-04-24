# Method 1: Using recursion
'''def lcs(s, t, n, m):
    if n == 0 or m == 0:
        return 0
    if s[n - 1] == t[m - 1]:
        return 1 + lcs(s, t, n - 1, m - 1)
    else:
        return max(lcs(s, t, n - 1, m), lcs(s, t, n, m - 1))


s_string = "abcde"
t_string = "ace"
print("LCS:", lcs(s_string, t_string, len(s_string), len(t_string)))'''

# Method 2: Using Memoization Approach

'''def lcs(s, t, m, n):
    # Base case: If either string has a length of 0, LCS length is 0
    if m == 0 or n == 0:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    if s[m - 1] == t[n - 1]:
        dp[m][n] = 1 + lcs(s, t, m-1, n-1)
    else:
        dp[m][n] = max(lcs(s, t, m - 1, n), lcs(s, t, m, n - 1))

    return dp[m][n]


s_string = "abcde"
t_string = "ace"
dp = [[-1] * (len(t_string) + 1) for _ in range(len(s_string) + 1)]
print("LCS:", lcs(s_string, t_string, len(s_string), len(t_string)))'''


# Method 3: Using Top Down DP Approach

def lcs(text1, text2, x, y):
    # Base case: If either string has a length of 0, LCS length is 0

    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[x][y]


s_string = "abcde"
t_string = "ace"

print("LCS:", lcs(s_string, t_string, len(s_string), len(t_string)))
