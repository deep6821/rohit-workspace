def printDiagonalSums(mat, n):
    principal = 0
    secondary = 0
    for i in range(0, n):
        principal += mat[i][i]
        secondary += mat[i][n - i - 1]

    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)


# Driver code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]
printDiagonalSums(a, 4)
