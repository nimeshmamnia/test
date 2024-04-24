'''Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Hint: Longest Palindromic Subsequence of String A is a Longest Common Subsequence of String A and reverse of String A'''


def lps(text1, text2, x, y):
    # Base case: If either string has a length of 0, LCS length is 0

    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[x][y]


s_string = "cbbd"
t_string = ''.join(reversed(s_string))

print("Longest Palindromic Subsequence:", lps(s_string, t_string, len(s_string), len(t_string)))
