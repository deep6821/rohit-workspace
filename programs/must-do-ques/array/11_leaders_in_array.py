"""
An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader.

For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
"""


# Time Complexity: O(n*n)
def find_leaders(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] <= arr[j]:
                break

        if j == n - 1:
            print(arr[i], end=" ")


# Time Complexity: O(n)
def find_leaders2(arr):
    n = len(arr)
    max_from_right = arr[n-1]
    print(max_from_right)
    for i in range(n-2, -1, -1):
        if max_from_right < arr[i]:
            print(arr[i])
            max_from_right = arr[i]


arr = [16, 17, 4, 3, 5, 2]
find_leaders(arr)
