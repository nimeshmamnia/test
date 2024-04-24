def findAnagrams(s, p):
    N = len(s)
    K = len(p)
    i = j = ans = 0
    temp = []
    while j < N:
        temp.append(s[j])
        if j - i + 1 < K:
            j += 1
        elif j - i + 1 == K:
            temp_string = ''.join(sorted(temp))
            if temp_string == ''.join(sorted(p)):
                ans += 1
            temp.pop(0)
            i += 1
            j += 1
    return ans


string_s = "aabaaaba"
string_p = "aaba"
print("Number of anagrams = ", findAnagrams(string_s, string_p))
