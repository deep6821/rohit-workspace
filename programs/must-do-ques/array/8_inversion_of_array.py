"""
Count Inversions in an array
----------------------------
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is
already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the
maximum.

Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
"""


# Time Complexity: O(n^2), Two nested loops are needed to traverse the array from start to end.
# Space Compelxity:O(1), No extra space is required.
def inversion_count1(arr):
    n = len(arr)
    i = 0
    count = 0
    while i < len(arr) - 1:
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
        i += 1

    return count


def merge_inversion_count(arr, temp, left, mid, right):
    print(arr, temp, left, mid, right)


# Time Complexity: O(n log n)
# Space Compelxity:O(1)
def merge_sort(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        # print("mid -----", mid)
        count += merge_sort(arr, temp, left, mid)
        # print("count >>>>>", count)
        count += merge_sort(arr, temp, mid + 1, right)

        count += merge_inversion_count(arr, temp, left, mid, right)

    return count


def inversion_count2(arr):
    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n - 1)


# arr = [8, 4, 2, 1]
# arr = [3, 2, 1]
arr = [1, 20, 6, 4, 5]
# print(inversion_count1(arr))
print("\n+++++++++++++++++")
print(inversion_count2(arr))
