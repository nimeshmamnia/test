'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''


def lps(nums1, nums2, x, y):
    # Base case: If either string has a length of 0, LCS length is 0

    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    longest_length = 0
    string_lps = ''
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                longest_length = max(longest_length, dp[i][j])
            else:
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = 0
    i = x
    j = y
    while i > 0 and j > 0:
        if nums1[i - 1] == nums2[j - 1]:
            string_lps = nums1[i - 1] + string_lps
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return longest_length, string_lps


s_string = "babad"
t_string = "dabab"

print("Longest Palindromic substring length:", lps(s_string, t_string, len(s_string), len(t_string)))