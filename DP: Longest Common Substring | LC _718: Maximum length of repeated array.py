'''LC problem: Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].'''

# combining 2 programs in one where we will be printing the longest common substring (its length and string itself)

# Method 1: Using recursion ..
'''
def lcs_recursion(str1, str2, m, n, count):
    if m == 0 or n == 0:
        return 0
    elif str1[m - 1] == str2[n - 1]:
        count = lcs_recursion(str1, str2, m - 1, n - 1, count + 1)
    else:
        count = max(count, lcs_recursion(str1, str2, m - 1, n, 0), lcs_recursion(str1, str2, m, n - 1, 0))

    return count


s_string = "babad"
t_string = "dabab"
count = 0

print("Longest Common substring length:", lcs_recursion(s_string, t_string, len(s_string), len(t_string), count))
'''


# Method 2: Using DP Approach
def lcs(nums1, nums2, x, y):
    # Base case: If either string has a length of 0, LCS length is 0

    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    longest_length = 0
    string_lcs = ''
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
            string_lcs = nums1[i - 1] + string_lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(string_lcs)

    return longest_length


s_string = "babad"
t_string = "dabab"

print("Longest Common substring length:", lcs(s_string, t_string, len(s_string), len(t_string)))
