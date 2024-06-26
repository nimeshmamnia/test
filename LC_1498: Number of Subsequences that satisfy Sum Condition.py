"""You are given an array of integers nums and an integer target. Return the number of non-empty subsequences of nums
such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too
large, return it modulo 109 + 7.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61). """


class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        M = int(1e9) + 7
        length = len(nums)
        left = 0
        right = length - 1
        nums.sort()
        count = 0
        pow = [1] * length
        for i in range(1, length):
            pow[i] = (pow[i - 1] * 2) % M

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1

            else:
                count = (count + pow[right - left]) % M
                left += 1

        return count
