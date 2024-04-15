def min_diff(array_func):
    arr = sorted(array_func)
    diff1 = float('inf')
    for i in range(len(arr) - 1):
        diff2 = arr[i + 1] - arr[i]
        diff1 = min(diff1, diff2)
    return diff1


array = [5, 32, 45, 4, 12, 18, 25]
print("Minimum Difference is: ", min_diff(array))
