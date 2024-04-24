'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''


def findequalsum(arr, target):
    if target % 2 != 0:
        return False
    else:
        target = target // 2

        # Creating a 2D DP array and initializing it.
        t = [[False] * (target + 1) for _ in range(len(arr) + 1)]

        for i in range(len(arr) + 1):
            t[i][0] = True

        for i in range(1, len(arr) + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]

    return t[len(arr)][target]


arr1 = [1, 5, 5, 11]
target1 = sum(arr1)
print("Does given array is equal sum partition:", findequalsum(arr1, target1))

# Recursive Approach ..

'''def can_partition(nums, target):
    if target == 0:
        return True
    if target < 0 or not nums:
        return False
    return can_partition(nums[:-1], target - nums[-1]) or can_partition(nums[:-1], target)

def findequalsum(arr, target):
    if target % 2 != 0:
        return False
    else:
        target //= 2
        return can_partition(arr, target)

arr1 = [1, 5, 5, 11]
target1 = sum(arr1)
print("Does given array have an equal sum partition:", findequalsum(arr1, target1))
'''
