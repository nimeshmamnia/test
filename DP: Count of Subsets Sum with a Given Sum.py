def countsubsets(arr, target):
    # Initialize 2D DP table
    t = [[0] * (target + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        t[i][0] = 1

    # Fill with rest of the table
    for i in range(1, len(arr) + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][target]


arr1 = [2, 3, 5, 6, 8, 10]
value = 10
print("Number of subsets which can add up to", value, "are:", countsubsets(arr1, value))
