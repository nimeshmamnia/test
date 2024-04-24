'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        sum = 0
        result = float('inf')
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                sum -= nums[i]
                result = min(result, j - i + 1)
                i += 1
            j += 1
        if result == float('inf'):
            return 0
        else:
            return result
