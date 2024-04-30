'''
Given an array arr[] of size N and a given difference diff, the task is to count the number of partitions that we can
perform such that the difference between the sum of the two subsets is equal to the given difference.
Note: A partition in the array means dividing an array into two parts say S1 and S2 such that the union of S1 and S2 is
equal to the original array and each element is present in only of the subsets.

Examples:
Input: N = 4, arr[] = [5, 2, 6, 4], diff = 3
Output: 1
Explanation: We can only have a single partition which is shown below:
{5, 2} and {6, 4} such that S1 = 7 and S2 = 10 and thus the difference is 3

Input: N = 5, arr[] = [1, 2, 3, 1, 2], diff = 1
Output: 5
Explanation: We can have five partitions which is shown below
{1, 3, 1} and {2, 2} – S1 = 5, S2 = 4
{1, 2, 2} and {1, 3} – S1 = 5, S2 = 4
{3, 2} and {1, 1, 2} – S1 = 5, S2 = 4
{1, 2, 2} and {1, 3} – S1 = 5, S2 = 4
{3, 2} and {1, 1, 2} – S1 = 5, S2 = 4
'''
'''
Problem Transformation
Given an array and a difference diff, if S1 and S2 are the sums of the two subsets, then:
S1−S2= diff
S1+S2 = sum(array)
From these equations we can derive -> S1 = (sum(array) + diff) // 2. This means we need to count the subsets of the 
array which sum up to S1. This is feasible if (diff + sum) is even (since S1 needs to be an integer). 
If (diff + sum) is odd, it's impossible to split the array as required, so the result should be 0.'''
import sys

# Method 1: Using recursive approach:
'''def count_subsets(arr, n, sum):
    # Base cases
    if sum == 0:
        return 1  # There's always one way to get sum 0, i.e., take no elements
    if n == 0:
        return 0  # No way to get a non-zero sum from zero elements

    # If the last element is greater than the sum, ignore it
    if arr[n - 1] > sum:
        return count_subsets(arr, n - 1, sum)

    # Include the last element or exclude it
    return count_subsets(arr, n - 1, sum) + count_subsets(arr, n - 1, sum - arr[n - 1])


def find_ways(arr, n, diff):
    total_sum = sum(arr)
    # Check if (diff + sum) is odd or if diff > sum, partition isn't possible
    if (diff + total_sum) % 2 != 0 or diff > total_sum:
        return 0
    subset_sum = (diff + total_sum) // 2
    return count_subsets(arr, n, subset_sum)


# Example usage
N1 = 4
arr1 = [5, 2, 6, 4]
diff1 = 3
print("Number of partitions:", find_ways(arr1, N1, diff1))

N2 = 5
arr2 = [1, 2, 3, 1, 2]
diff2 = 1
print("Number of partitions:", find_ways(arr2, N2, diff2))'''


# Method 2: Using DP Approach
def count_subsets(arr, value):
    # Base Conditions - Initializing first row and first column of 2D DP table
    t = [[0] * (value + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        t[i][0] = 1

    for i in range(1, len(arr) + 1):
        for j in range(1, value + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][value]


def find_ways(arr, n, diff):
    total_sum = sum(arr)
    # Check if (diff + sum) is odd or if diff > sum, partition isn't possible
    if (diff + total_sum) % 2 != 0 or diff > total_sum:
        return 0
    subset_sum = (diff + total_sum) // 2
    return count_subsets(arr, subset_sum)


N1 = 4
arr1 = [5, 2, 6, 4]
diff1 = 3
print("Number of partitions:", find_ways(arr1, N1, diff1))

N2 = 5
arr2 = [1, 2, 3, 1, 2]
diff2 = 1
print("Number of partitions:", find_ways(arr2, N2, diff2))
