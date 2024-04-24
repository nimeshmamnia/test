def longestsubstring(fruits, k):
    i = j = 0
    temp = dict()
    max_size = 0
    while j < len(fruits):
        temp[fruits[j]] = temp.get(fruits[j], 0) + 1
        if len(temp) < k:
            j += 1
        elif len(temp) == k:
            max_size = max(max_size, j - i + 1)
            j += 1
        while len(temp) > k:
            temp[fruits[i]] -= 1
            if temp[fruits[i]] == 0:
                del temp[fruits[i]]
            i += 1
            j += 1
    return max_size

string_a = "aabacbebebe"
unique_char_size = 3
print("Longest substring with K unique characters is: ", longestsubstring(string_a, unique_char_size))
