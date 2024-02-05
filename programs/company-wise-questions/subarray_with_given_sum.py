def subarray_with_given_sum(arr, s):
    n = len(arr)
    for i in range(0, n):
        current_sum = arr[i]
        j = i + 1
        while j <= n:
            if current_sum == s:
                print("Sum found between: ", i, j - 1)
                return

            if current_sum > s or j == n:
                break

            current_sum = current_sum + arr[j]
            j += 1


if __name__ == "__main__":
    # arr = [1, 2, 3, 7, 5]
    # s = 12

    arr = list(map(int, input().split()))  # [15, 2, 4, 8, 9, 5, 10, 23]
    s = int(input())  # 23
    subarray_with_given_sum(arr, s)
