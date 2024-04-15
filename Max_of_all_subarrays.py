def max_subarray(nums, k):
    N = len(nums)
    i = j = 0
    temp = []
    result = []
    if N == 0:
        return 0

    while j < N:
        while len(temp) > 0 and temp[-1] < nums[j]:
            temp.pop(-1)
        temp.append(nums[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            result.append(temp[0])
            if temp[0] == nums[i]:
                temp.pop(0)
            i += 1
            j += 1

    return result
