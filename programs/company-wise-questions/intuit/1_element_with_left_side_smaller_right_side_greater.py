# Time Complexity: O(n)
# Auxiliary Space: O(n)


def find_element(arr):
    n = len(arr)
    # left_max[i] stores maximum of arr[0..i-1]
    left_max = [None] * n
    left_max[0] = float('-inf')
    # Fill left_max[1..n-1]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i - 1])

    # Initialize minimum from right
    right_min = float('inf')
    # Traverse array from right
    for i in range(n - 1, -1, -1):
        if left_max[i] < arr[i] < right_min:
            return i
        right_min = min(right_min, arr[i])

    return -1


if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    print(find_element(arr))
