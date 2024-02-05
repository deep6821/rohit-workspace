"""
Count all possible paths from top left to bottom right of a mXn matrix
The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that
from each cell you can either move only to right or down

Examples :

Input :  m = 2, n = 2;
Output : 2

There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)
"""


# The time complexity of above recursive solution is exponential.
def number_of_paths_recursively(m, n):
    if m == 1 or n == 1:
        return 1

    # total number of path = top(m-1, n) - down(m, n-1)
    return number_of_paths_recursively(m - 1, n) + number_of_paths_recursively(m, n - 1)


print(number_of_paths_recursively(3, 3))


#  Time complexity: O(mn) and space complexity: O(mn).
def number_of_paths1(m, n):
    count = [[0 for x in range(m)] for y in range(n)]
    print(count)

    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


#  Time complexity: O(mn) and space complexity: O(n).
def number_of_paths2(p, q):
    # Create a 1D array to store results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]


# Driver Code
print(number_of_paths1(3, 3))
print(number_of_paths2(3, 3))
