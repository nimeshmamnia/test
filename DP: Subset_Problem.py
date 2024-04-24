def findsubset(arr, target):
    # Create a (len(arr) + 1) by (target + 1) 2D list initialized with False
    t = [[False] * (target + 1) for _ in range(len(arr) + 1)]

    # Base condition: it's always possible to make the sum 0 (by choosing no element)
    for i in range(len(arr) + 1):
        t[i][0] = True

    # Fill the DP table
    for i in range(1, len(arr) + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][target]


# Example usage
arr1 = [2, 3, 7, 8, 10]
target1 = 11
print("Is there a subset with sum equal to target?", findsubset(arr1, target1))
