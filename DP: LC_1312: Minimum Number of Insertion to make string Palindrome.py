'''Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".'''


def minInsertions(s):
    x = len(s)
    t = ''.join(reversed(s))
    dp = [[0] * (x + 1) for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Minimum number of deletion = Minimum number of insertion = len(x) - len(lps)
    return x - dp[x][x]


print(minInsertions("zbzazz"))
