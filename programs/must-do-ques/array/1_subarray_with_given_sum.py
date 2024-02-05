"""
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices: 20 + 3 + 10 = 33
"""


# TC: O(n^2) in worst case and SC: 0(1)
def subarray_sum(arr, s):
    result = []
    n = len(arr)
    for i in range(0, n):
        curr_sum = arr[i]
        j = i + 1
        while j <= n:
            if curr_sum == s:
                print("Sum found between {} and {}".format(i, j - 1))
                result.append((i, j-1))
                # return 1

            if curr_sum > s or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print(result)
    print("No subarray found")
    return 0


# TC: 0(n) and SC: 0(1)
def subarray_sum2(arr, s):
    n = len(arr)
    curr = arr[0]
    i = 1
    start = 0
    while i <= n:
        while curr > s and start < i - 1:
            curr = curr - arr[start]
            start += 1

        if curr == s:
            print("Sum found between {} and {}".format(start, i - 1))
            return 1

        if i < n:
            curr = curr + arr[i]

        i += 1

    print("No subarray with given sum exists")


# Time complexity: O(n).
# Auxiliary space: O(n)
def subarray_sum_for_negative_no(arr, s):
    n = len(arr)
    dict = {}
    curr = 0
    for i in range(0, n):
        curr = curr + arr[i]

        if curr == s:
            print("Sum found between indexes 0 to", i)
            return

        if (curr - s) in dict:
            print("Sum found between indexes", dict[curr - s] + 1, "to", i)
            return
        dict[curr] = i

    print("No subarray with given sum exists")


arr = [1, 2, 3, 4 , 5]
subarray_sum([4, 8, 1, 3, 9, 5, 11], 10)
subarray_sum(arr, s=5)
subarray_sum2(arr, s=33)
subarray_sum_for_negative_no([10, 2, -2, -20, 10], s=-10)
