"""
i/p: [1, 2, 3, 4, 5, 6]
o/p: [6, 1, 5, 2, 4, 3]
"""


# Time Complexity: O(n)
# Auxiliary Space: O(n)
def rearrange_array_in_max_min_form(arr):
    n = len(arr)
    start = 0
    end = n - 1
    temp = [None] * n
    flag = True

    for i in range(n):
        if flag:
            temp[i] = arr[end]
            end -= 1
        else:
            temp[i] = arr[start]
            start += 1
        flag = bool(1 - flag)

    print(temp)


arr = [1, 2, 3, 4, 5, 6]
rearrange_array_in_max_min_form(arr)
