'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
'''

# Method 1: Using recursive approach:
'''def minimumsum(arr, length, calculated_sum, total_sum):
    if length == 0:
        return abs((total_sum - calculated_sum) - calculated_sum)

    return min(minimumsum(arr, length - 1, calculated_sum + arr[length - 1], total_sum),
               minimumsum(arr, length - 1, calculated_sum, total_sum))


arr1 = [1, 6, 11, 5]
length1 = len(arr1)
total_sum1 = sum(arr1)
print("Minimum Sum difference of given array is:", minimumsum(arr1, length1, 0, total_sum1))'''


# Method 2: Using DP approach:

def minimumsum(arr, target):
    # Initialize 2D DP table
    t = [[False] * (target + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        t[i][0] = True

    # Fill with rest of the table
    for i in range(1, len(arr) + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    # return t[len(arr)][target]
    result = float('inf')
    for j in range((target // 2) + 1):
        if t[len(arr)][j] == 1:
            result = min(result, abs(target - 2 * j))

    return result


arr1 = [1, 12, 11, 5]
total_sum1 = sum(arr1)
print("Minimum Sum difference of given array:", minimumsum(arr1, total_sum1))
