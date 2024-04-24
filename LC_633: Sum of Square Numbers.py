'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false '''

import math


def judgeSquareSum(c):
    # Base Case
    if c == 0:
        return True

    left = 0
    right = int(math.sqrt(c))

    while left <= right:
        sumofsquares = left * left + right * right
        if sumofsquares == c:
            return True
        elif sumofsquares < c:
            left += 1
        else:
            right -= 1

    return False


print(judgeSquareSum(15))
