"""
Input : 1 0 0 1 0 1 0 1 1 1 1 1 1 0 0 1 1 0 1 0 0
Output : 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
Explanation: The output is a sorted array of 0 and 1

Approach: This concept is related to partition of quick sort . In quick sort’
partition, after one scan, the left of the array is smallest and
right of the array is the largest of selected pivot element.
"""


# Time Complexity: O(n)
# Space Complexity:O(1)
def sort_a_binary_array(arr, n):
    i = -1
    for j in range(n):
        # if number is smaller than 1 then swap it with j-th number
        if arr[j] < 1:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]


if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    n = len(arr)
    sort_a_binary_array(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
