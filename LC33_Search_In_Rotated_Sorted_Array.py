class Solution(object):

    def binarysearch(self, nums, target, start, end):
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def findmin(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return start

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        minimum_index = self.findmin(nums)

        # Once we know the smallest element index, we determine which half to binary search.
        if target == nums[minimum_index]:
            return minimum_index
        if target >= nums[minimum_index] and target <= nums[-1]:
            return self.binarysearch(nums, target, minimum_index, len(nums) - 1)
        else:
            return self.binarysearch(nums, target, 0, minimum_index - 1)


# Example usage:
sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Index of target:", sol.search(nums, target))  # Output should be the index of '0' in nums
