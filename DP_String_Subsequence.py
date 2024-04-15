def is_subsequence(t, s, m, n):
    # Base Conditions
    if m == len(s):
        return True
    if n == len(t):
        return False

    # Comparing index by index
    if t[n] == s[m]:
        return is_subsequence(t, s, m + 1, n + 1)
    else:
        return is_subsequence(t, s, m, n + 1)


t_string = "axbvsckmdle"
s_string = "acb"

if is_subsequence(t_string, s_string, 0, 0):
    print(True)
else:
    print(False)
