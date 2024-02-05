"""
Can be used to find the longest common substring in O(m*n) time. The idea is to find length of the longest
common suffix for all substrings of both strings and store these lengths in a table.

The longest common suffix has following optimal substructure property:
If last characters match, then we reduce both lengths by 1
LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
If last characters do not match, then result is 0, i.e.,
LCSuff(X, Y, m, n) = 0 if (X[m-1] != Y[n-1])

Now we consider suffixes of different substrings ending at different indexes.
The maximum length Longest Common Suffix is the longest common substring.
LCSubStr(X, Y, m, n) = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m and 1 <= j <= n
"""


# Time Complexity: O(m*n) Auxiliary Space: O(m*n) ---> DP
def longest_common_substring(x, y):
    m = len(x)
    n = len(y)
    lcs_suff = [[0 for k in range(n + 1)] for l in range(m + 1)]
    print(lcs_suff)
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if x[i - 1] == y[j - 1]:
                lcs_suff[i][j] = lcs_suff[i - 1][j - 1] + 1
                result = max(result, lcs_suff[i][j])
            else:
                lcs_suff[i][j] = 0
    return result


def lcs(x, y):
    temp_arr = [[0 for i in range(10)] for j in range(10)]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                temp_arr[i][j] = 1 + temp_arr[i - 1][j - 1]
            else:
                temp_arr[i][j] = max(temp_arr[i - 1][j], temp_arr[i][j - 1])
    return temp_arr[i][j]


x = 'abcdxyz'
y = 'xyzabcd'

# x = 'OldSite:GeeksforGeeks.org'
# y = 'NewSite:GeeksQuiz.com'
print(longest_common_substring(x, y))

x = "eg"
y = "defg"
print(lcs(x, y))
