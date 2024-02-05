"""
Given an array arr[] of N elements where N ≥ 2, the task is to check the type
of array whether it is:
1. Increasing.
2. Decreasing.
3. Increasing then decreasing.
4. Decreasing then increasing.

Note that the given array is definitely one of the given types.

Examples:
Input: arr[] = {1, 2, 3, 4, 5}
Output: Increasing
Input: arr[] = {1, 2, 4, 3}
Output: Increasing then decreasing

Approach: The following conditions must satisfy for:
1. Increasing array: The first two and the last two elements must be in
   increasing order.
2. Decreasing array: The first two and the last two elements must be in
   decreasing order.
3. Increasing then decreasing array: The first two elements must be in
   increasing order and the last two elements must be in decreasing order.
4. Decreasing then increasing array: The first two elements must be in
   decreasing order and the last two elements must be in increasing order.
"""


def check_type(arr, n):
    # If the first two and the last two elements
    # of the array are in increasing order
    if arr[0] <= arr[1] and arr[n - 2] <= arr[n - 1]:
        print("Increasing")

    # If the first two and the last two elements
    # of the array are in decreasing order
    elif arr[0] >= arr[1] and arr[n - 2] >= arr[n - 1]:
        print("Decreasing")

    # If the first two elements of the array are in increasing order and the
    # last two elements of the array are in decreasing order
    elif arr[0] <= arr[1] and arr[n - 2] >= arr[n - 1]:
        print("Increasing then decreasing")

    # If the first two elements of the array are in decreasing order and the
    # last two elements of the array are in increasing order
    else:
        print("Decreasing then increasing")


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    check_type(arr, n)
