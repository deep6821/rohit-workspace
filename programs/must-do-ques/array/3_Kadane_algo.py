"""
Largest Sum Contiguous Subarray:
--------------------------------

i/p: [-2, -3, 4, -1, -2, 1, 5, -3]
o/p: 4+(-1)+(-2)+1+5 = 7
"""


# Time Complexity: O(n)
def max_subarray_sum(arr):
    m = 0  # keep track of maximum sum contiguous segment among all positive segments
    n = 0  # look for all positive contiguous segments of the array
    for i in range(0, len(arr)):
        n = n + arr[i]
        if n < 0:
            n = 0
        if m < n:
            m = n
    return m

# Time Complexity: O(n)
def max_subarray_sum2(arr):
    m = arr[0]
    curr_max = arr[0]
    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        m = max(m, curr_max)

    return m


# Function to find the maximum contiguous subarray and print its starting and end index
def max_subarray_sum3(arr):
    m, n, start, end, sum = 0, 0, 0, 0, 0
    for i in range(0, len(arr)):
        n += arr[i]
        if n < 0:
            n = 0
            sum = i + 1

        if m < n:
            m = n
            start = sum
            end = i

    print("Maximum contiguous sum is: {}".format(m))
    print("Starting and ending indexes are: {} and {}".format(start, end))


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(arr))
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(max_subarray_sum2(arr))
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray_sum3(arr)
