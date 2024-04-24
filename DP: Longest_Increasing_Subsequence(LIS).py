def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    # Initialize the DP array with 1 since the smallest LIS ending at each element is the element itself
    dp = [1] * len(nums)

    # Fill the DP array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence is the maximum value in the DP array
    return max(dp)


# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of the Longest Increasing Subsequence:", longest_increasing_subsequence(nums))
