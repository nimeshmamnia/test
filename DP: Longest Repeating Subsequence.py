'''Given a string, find the length of the longest repeating subsequence, such that the two subsequences don’t have same
string character at the same position, i.e. any ith character in the two subsequences shouldn’t have the same index in
the original string.
Examples:
Input: str = "abc"
Output: 0
There is no repeating subsequence

Input: str = "aab"
Output: 1
The two subsequence are 'a'(first) and 'a'(second). Note that 'b' cannot be considered as part of subsequence as it
would be at same index in both.

Input: str = "aabb"
Output: 2

Input: str = "axxxy"
Output: 2'''


def longestrepeatingsubsequence(text1):
    x = len(text1)
    repeating_subsequence = ''
    dp = [[0] * (x + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if text1[i - 1] == text1[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = x, x
    while i > 0 and j > 0:
        if text1[i - 1] == text1[j - 1] and i != j:
            repeating_subsequence = text1[i - 1] + repeating_subsequence
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # repeating_subsequence = repeating_subsequence + text1[i - 1]
            i -= 1
        else:
            # repeating_subsequence = repeating_subsequence + text2[j - 1]
            j -= 1

    return dp[x][x], repeating_subsequence


string1 = "aabb"
#string2 = "aabcbcdd"
length, subsequence = longestrepeatingsubsequence(string1)
print("Longest Repeating Subsequence Length:", length)
print("Longest Repeating Subsequence:", subsequence)
