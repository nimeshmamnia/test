'''You are given an array of integers nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding
window moves right by one position. Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]'''


def max_subarray(nums, k):
    N = len(nums)
    i = j = 0
    temp = []
    result = []
    if N == 0:
        return 0

    while j < N:
        while len(temp) > 0 and temp[-1] < nums[j]:
            temp.pop(-1)
        temp.append(nums[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            result.append(temp[0])
            if temp[0] == nums[i]:
                temp.pop(0)
            i += 1
            j += 1

    return result
