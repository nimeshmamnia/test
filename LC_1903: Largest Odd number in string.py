'''

Problem:
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a
non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
--------------------------------------------------------------
Solution:

Intuition
The problem seems to involve finding the largest odd number from a given numeric string. The approach likely involves
iterating through the string from right to left and stopping when an odd digit is encountered. The result should then be
 the substring from the beginning of the input string to the position where the odd digit was found.

Approach
The provided code seems to follow the intuition correctly. It initializes an empty string result and iterates through
the input numeric string num from right to left. For each digit, it checks if it's odd, and if so, it updates the result
 to be the substring from the beginning of the input string to the current position. The loop breaks as soon as an odd
 digit is found.

Complexity
Time complexity: (O(n)), where (n) is the length of the input string num. In the worst case, the algorithm may iterate
through the entire string once.
Space complexity: (O(1)), as the algorithm only uses a constant amount of extra space regardless of the input size.
The primary variable is result, which is a string holding the final result.

'''


def largestOddNumber(num):
    """
    :type num: str
    :rtype: str
    """
    ln = len(num) - 1
    for i in range(ln, -1, -1):
        ch = num[i]
        if int(ch) % 2 != 0:
            return num[:i + 1]

    return ""


print(largestOddNumber("532"))
print(largestOddNumber("32567"))
print(largestOddNumber("55"))
print(largestOddNumber("52"))
print(largestOddNumber("100"))
