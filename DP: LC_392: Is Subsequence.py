def issubsequence(text1, text2):
    x, y = len(text1), len(text2)
    lcs = ''
    dp = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = x, y
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs = text1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[x][y], lcs


string1 = "abc"
string2 = "ahbgdc"
length, subsequence = issubsequence(string1, string2)
print("Longest Repeating Subsequence Length:", length)
print("Longest Repeating Subsequence:", subsequence)

if subsequence == string1:
    print(True)
else:
    print(False)