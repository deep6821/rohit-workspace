"""
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements
at higher indexes. For example, in an array A:

Example :
    Input: A[] = {-7, 1, 5, 2, -4, 3, 0}
    Output: 3

    3 is an equilibrium index, because:
    A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
"""

# Time Complexity: O(n)
def equilibrium_index(arr):
    total_sum = sum(arr)
    print(total_sum)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum = total_sum - num
        if left_sum == total_sum:
            return i
        left_sum += num
    return -1


arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(arr))
