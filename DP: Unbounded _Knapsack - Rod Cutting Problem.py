# Method 1: Using recursion
def rod_cutting(weight, n, value, W):
    if n == 0 or W == 0:
        return 0
    if weight[n - 1] <= W:
        return max(value[n - 1] + rod_cutting(weight, n - 1, value, W - weight[n - 1]),
                   rod_cutting(weight, n - 1, value, W))
    else:
        return rod_cutting(weight, n - 1, value, W)


price = [1, 5, 8, 9, 10, 17, 17, 20]
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 8
n = len(arr)
print("Maximum Profit will be:", rod_cutting(arr, n, price, target))

# Method 2: Using DP

'''def rod_cutting(arr, n, value, W):
    t = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][W]'''
