def threeSum(nums):
    '''
    Algorithm Explanation:

1. Sort the Array: Sorting the array enables a two-pointer technique.
2. Iterate with a Fixed Point: Fix one number and use two other pointers to find the remaining two numbers.
3. Two Pointers for Remaining Two: Initialize one pointer at the start (just next to the fixed point) and another at the
   end of the array. Move these pointers based on the sum compared to zero.
4. Skip Duplicates: Ensure that the same triplets are not included multiple times by skipping duplicates for each
    pointer.

    :param nums: list
    :return: list
    '''
    nums.sort()  # Sort the array
    res = []  # This will store the result triplets

    for i in range(len(nums) - 2):  # We need at least three numbers to continue
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements for the first pointer
            continue

        left, right = i + 1, len(nums) - 1  # Initialize two pointers

        while left < right:
            total = nums[i] + nums[left] + nums[right]  # Calculate the sum of three numbers

            if total < 0:  # If the sum is less than zero, move the left pointer to the right to increase the sum
                left += 1
            elif total > 0:  # If the sum is more than zero, move the right pointer to the left to decrease the sum
                right -= 1
            else:  # If the sum is zero, we found a triplet
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # Skip duplicates for the second pointer
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # Skip duplicates for the third pointer
                    right -= 1
                left += 1  # Move both pointers to look for the next unique triplet
                right -= 1

    return res


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
