def longestsubstring(nums, k):
    i = j = 0
    temp = dict()
    max_size = 0
    while j < len(nums):
        temp[nums[j]] = temp.get(nums[j], 0) + 1
        if len(temp) < k:
            j += 1
        elif len(temp) == k:
            max_size = max(max_size, j - i + 1)
            j += 1
        while len(temp) > k:
            temp[nums[i]] -= 1
            if temp[nums[i]] == 0:
                del temp[nums[i]]
            i += 1
            j += 1
    return max_size

string_a = "aabacebebebe"
unique_char_size = 3
print("Longest substring with K unique characters is: ", longestsubstring(string_a, unique_char_size))
