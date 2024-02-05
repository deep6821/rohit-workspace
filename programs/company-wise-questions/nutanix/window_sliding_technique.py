"""
This technique shows how a nested for loop in some problems can be converted to
a single for loop to reduce the time complexity.

Let’s start with a problem for illustration where we can apply this technique:
Given an array of integers of size ‘n’. Our aim is to calculate the maximum sum
of ‘k’ consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700
"""
import sys

# INT_MIN = -sys.maxsize - 1
INT_MIN = 0


# Brute Force Approach
def maximum_sum(arr, k):
    n = len(arr)
    max_sum = INT_MIN
    for i in range(n - k + 1):
        curr_sum = 0
        for j in range(k):
            curr_sum = curr_sum + arr[i + j]
        max_sum = max(curr_sum, max_sum)
    return max_sum


"""
Window Sliding Technique:
The technique can be best understood with the window pane in bus, consider a 
window of length n and the pane which is fixed in it of length k. 

Consider, initially the pane is at extreme left i.e., at 0 units from the left. 
Now, co-relate the window with array arr[] of size n and pane with current_sum 
of size k elements. Now, if we apply force on the window such that it moves a 
unit distance ahead. The pane will cover next k consecutive elements. 

Consider an array arr[] = {5, 2, -1, 0, 3} and value of k = 3 and n = 5

Applying sliding window technique:
1. We compute the sum of first k elements out of n terms using a linear loop 
and store the sum in variable window_sum.
2. Then we will graze linearly over the array till it reaches the end and 
simultaneously keep track of maximum sum.
3. To get the current sum of block of k elements just subtract the first 
element from the previous block and add the last element of the current block.
"""


def maximum_sum1(arr, k):
    n = len(arr)
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    # Compute the sums of remaining windows by removing first element of
    # previous window and adding last element of the current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


print(maximum_sum([100, 200, 300, 400], 2))
print(maximum_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
