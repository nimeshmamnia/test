'''Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted at some another point.

Example 1:
Input :
str1 = "heap", str2 = "pea"
Output :
Minimum Deletion = 2 and
Minimum Insertion = 1
Explanation:
p and h deleted from heap. Then, p is inserted at the beginning
One thing to note, though p was required yet
it was removed/deleted first from its position and
then it is inserted to some other position.
Thus, p contributes one to the deletion_count
and one to the insertion_count.'''


def minimumdeletionaddition(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j-1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


str1 = "heap"
str2 = "pea"

print('Minimum Deletion:', len(str1) - minimumdeletionaddition(str1, str2))
print('Minimum Addition:', len(str2) - minimumdeletionaddition(str1, str2))

