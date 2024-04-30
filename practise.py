def lcs(s, t, m, n):
    # Base case: If either string has a length of 0, LCS length is 0
    if m == 0 or n == 0:
        return 0

    if dp[m][n] != 0:
        return dp[m][n]

    if s[m - 1] == t[n - 1]:
        dp[m][n] = 1 + lcs(s, t, m-1, n-1)
    else:
        dp[m][n] = max(lcs(s, t, m - 1, n), lcs(s, t, m, n - 1))

    return dp[m][n]


s_string = "abcde"
t_string = "abf"
dp = [[0] * (len(t_string) + 1) for _ in range(len(s_string) + 1)]
print("LCS:", lcs(s_string, t_string, len(s_string), len(t_string)))