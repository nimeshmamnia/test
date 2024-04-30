"""Given an array of integers nums and an integer k, return the total number of sub-arrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2"""


# def subarraySum(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     i = add = j = 0
#     count = max_size = 0
#     while j < len(nums):
#         add += nums[j]
#         while add > k:
#             add -= nums[i]
#             i += 1
#         if add == k:
#             count += 1    # To count number of sub arrays of sum 5
#             max_size = max(max_size, j - i + 1)
#         j += 1
#     return max_size
#
#
# nums1 = [1, 2, 3]
# k1 = 3
# print("Number of subarrays = ", subarraySum(nums1, k1))

def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    i = add = j = 0
    count = 0
    negative = 0
    while j < len(nums):
        add += nums[j]

        # Check if the current sum matches k and count if it does
        while add >= k and i <= j:
            if add == k:
                count += 1
                negative = 1
            # After checking, reduce the sum by removing nums[i] and increment i
            add -= nums[i]
            i += 1

        # Move to the next element in nums
        j += 1

    return count if negative else 1


# Example usage
nums1 = [-1, -1, 1]
k1 = 0
print("Number of sub-arrays = ", subarraySum(nums1, k1))
