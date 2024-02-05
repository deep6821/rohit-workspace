"""
Reverse an array in groups of given size:
-----------------------------------------

Given an array, reverse every sub-array formed by consecutive k elements.
Examples:
Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
Output:
[3, 2, 1, 6, 5, 4, 9, 8, 7]
"""


# Time complexity of above solution is O(n).
# Auxiliary space used by the program is O(1).
def reverse_array_in_groups1(arr, k):
    n = len(arr)
    i = 0
    while i < n:
        l = i
        r = min(i + k - 1, n - 1)
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        i += k
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(reverse_array_in_groups1(arr, k))
