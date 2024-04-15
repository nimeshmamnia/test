def twosum(arr, val):
    arr.sort()
    left = 0
    right = -1
    print("Pairs whose sums equal to the value are: ")
    while arr[left] < arr[right]:
        if arr[left] + arr[right] < val:
            left += 1
        elif arr[left] + arr[right] > val:
            right -= 1
        elif arr[left] + arr[right] == val:
            print("(", arr[left], ",", arr[right], ")")
            left += 1
            right -= 1


a = [5, 7, 4, 3, 9, 8, 19, 21]
value = int(input("Enter sum: "))
twosum(a, value)
