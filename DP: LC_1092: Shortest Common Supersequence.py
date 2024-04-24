'''Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"'''


def shortestCommonSupersequence(str1, str2):
    m, n = len(str1), len(str2)
    supersequence = ""
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            supersequence = supersequence + str1[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[j - 1][i]:
            supersequence = supersequence + str1[i - 1]
            i -= 1
        else:
            supersequence = supersequence + str2[j - 1]
            j -= 1

    while i > 0:
        supersequence = supersequence + str1[i - 1]
        i -= 1

    while j > 0:
        supersequence = supersequence + str2[j - 1]
        j -= 1

    print(''.join(reversed(supersequence)))
    return m + n - dp[m][n]


string_a = "AGGTAB"
string_b = "GXTXAYB"
print("Shortes Common Supersequence Length:", shortestCommonSupersequence(string_a, string_b))
