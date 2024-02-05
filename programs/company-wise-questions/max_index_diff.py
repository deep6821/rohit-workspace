def max_index_diff(arr):
    max_diff = -1
    n = len(arr)
    # temp = []
    # for i in range(n):
    #     j = i + 1
    #     while j <= n:
    #         if arr[i] < arr[j]:
    #             m = j - i
    #             temp.append(m)
    #
    #         if j == n:
    #             break
    # print(max(temp))
    for i in range(0, n):
        j = n - 1
        while j > i:
            if arr[j] > arr[i] and max_diff < j - i:
                max_diff = j - i

            j -= 1

    return max_diff


if __name__ == "__main__":
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    print(max_index_diff(arr))
