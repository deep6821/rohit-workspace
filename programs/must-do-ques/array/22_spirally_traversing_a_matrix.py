def spiral(arr, row, column):
    starting_row_index = 0
    ending_column_index = 0

    while starting_row_index < row and ending_column_index < column:
        for i in range(ending_column_index, column):
            print(arr[starting_row_index][i], end=" ")

        starting_row_index += 1

        for j in range(starting_row_index, row):
            print(arr[j][column - 1], end=" ")

        column -= 1

        if starting_row_index < row:
            for k in range(column - 1, (ending_column_index - 1), -1):
                print(arr[row - 1][k], end=" ")

            row -= 1

        if ending_column_index < column:
            for l in range(row - 1, starting_row_index - 1, -1):
                print(arr[l][ending_column_index], end=" ")

            ending_column_index += 1


arr = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]
row = 3
column = 6
spiral(arr, row, column)
