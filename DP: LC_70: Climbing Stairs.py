'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Explanation: This program uses Dynamic Programming concept. Please refer to program 1 of the video: https://www.youtube.com/watch?v=_i4Yxeh5ceQ&ab_channel=NeetCode
'''


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    one = two = 1

    for i in range(n - 1):
        temp = one + two
        one = two
        two = temp

    return temp


print(climbStairs(5))
