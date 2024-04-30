def longestsubstring(nums):
    i = j = 0
    temp = dict()
    max_size = 0
    while j < len(nums):
        temp[nums[j]] = temp.get(nums[j], 0) + 1
        while len(temp) < j-i+1:
            temp[nums[i]] -= 1
            if temp[nums[i]] == 0:
                del temp[nums[i]]
            i += 1
        if len(temp) == j-i+1:
            max_size = max(max_size, j - i + 1)
        j += 1
    return max_size


string_a = "pwwkew"
print("Longest substring with unique characters is: ", longestsubstring(string_a))
