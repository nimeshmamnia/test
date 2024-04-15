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
#             count += 1
#             max_size = max(max_size, j - i + 1)
#         j += 1
#     return count
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
    while j < len(nums):
        add += nums[j]

        # Check if the current sum matches k and count if it does
        while add >= k and i <= j:
            if add == k:
                count += 1
            # After checking, reduce the sum by removing nums[i] and increment i
            add -= nums[i]
            i += 1

        # Move to the next element in nums
        j += 1

    return count


# Example usage
nums1 = [-1, -1, 1]
k1 = 0
print("Number of subarrays = ", subarraySum(nums1, k1))

