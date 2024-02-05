"""
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.

Input:
A = [1,2,3,7,5]
N = 5, S = 12
Output: 2 4
Explanation: The sum of elements from 2nd position to 4th position is 12.
"""


# TC: O(n^2) in worst case and SC: 0(1)
def sub_array_with_given_sum1(arr, s):
    n = len(arr)
    arr_elements = []
    arr_indexes = []
    for i in range(0, n-1):
        current_sum = arr[i]
        j = i + 1
        while j <= n:
            if current_sum == s:
                print("Sum found between the indexes: {} {}".format(i, j - 1))
                arr_elements.append(arr[i: j])
                arr_indexes.append((i, j - 1))

            if current_sum > s or j == n:
                break

            current_sum = current_sum + arr[j]
            j += 1
    print("Array elements: ", arr_elements)
    print("Array Indexes: ", arr_indexes)


arr = [1, 2, 3, 7, 5]
s = 12
# arr = [3, 4, -7, 1, 3, 3, 1, -4]
# s = 7
sub_array_with_given_sum1(arr, s)
