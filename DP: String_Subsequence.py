def is_subsequence(t, s, m, n):
    # Base Conditions
    if m == len(s):
        return True
    if n == len(t):
        return False

    # Comparing index by index
    if t[n] == s[m]:
        return is_subsequence(t, s, m + 1, n + 1)
    else:
        return is_subsequence(t, s, m, n + 1)


t_string = "acbvsckmdle"
s_string = "acb"

if is_subsequence(t_string, s_string, 0, 0):
    print(True)
else:
    print(False)

# Method 2: Top Down DP Approach

'''def is_subsequence(s, t):
    s_len, t_len = len(s), len(t)
    dp = [[False] * (t_len + 1) for _ in range(s_len + 1)]

    # Base case: Empty string s is always a subsequence of any string t
    for j in range(t_len + 1):
        dp[0][j] = True

    # Fill the DP table
    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # If characters match, take the result from diagonal
            else:
                dp[i][j] = dp[i][j - 1]  # Otherwise, take the result from the left

    # Return the result from the bottom-right cell
    return dp[s_len][t_len]

t_string = "acbvsckmdle"
s_string = "acb"
print("Is s_string subsequence of t_string? :", is_subsequence(s_string, t_string))

'''
