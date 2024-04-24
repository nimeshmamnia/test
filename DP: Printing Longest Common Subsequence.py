def lcs(text1, text2, x, y):
    # Base case: If either string has a length of 0, LCS length is 0

    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    string_lcs = ""
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = x
    j = y
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            string_lcs = text1[i - 1] + string_lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return string_lcs


s_string = "abcde"
t_string = "ace"

print("LCS:", lcs(s_string, t_string, len(s_string), len(t_string)))
