'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
'''


def decodeways(s, n, i):
    if i == n:
        return 1
    if s[i] == '0':
        return 0

    result = decodeways(s, n, i + 1)
    if i + 1 < n:
        if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
            result = result + decodeways(s, n, i + 2)

    return result


string_s = "226"

print("Number of ways", string_s, "can be decoded are: ", decodeways(string_s, len(string_s), 0))

# Method 2: Recursion + Memoization

"""class Solution(object):
    def decodeways(self, s, n, i, memo):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]

        result = self.decodeways(s, n, i + 1, memo)
        if i + 1 < n:
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                result += self.decodeways(s, n, i + 2, memo)

        memo[i] = result
        return result

    def numDecodings(self, s):
        n = len(s)
        i = 0
        memo = {}
        return self.decodeways(s, n, i, memo)
"""
