"""
Approach:
- The 1-basic idea is to use a HashMap to solve the problem. But there is a catch, the numbers in the array
are from 0 to n-1, and the input array has length n. So, the input array can be used as a HashMap.
- While traversing the array, if an element a is encountered then increase the value of a%n‘th element by n.
- The frequency can be retrieved by dividing the a%n‘th element by n.

Algorithm:
1. Traverse the given array from start to end.
2. For every element in the array increment the arr[i]%n‘th element by n.
3. Now traverse the array again and print all those indices i for which arr[i]/n is greater than 1. Which
guarantees that the number n has been added to that index.

Time Complexity: O(n). Only two traversal is needed. So the time complexity is O(n)
Auxiliary Space: O(1). As no extra space is needed, so the space complexity is constant
"""


def find_duplicate_numbers(arr):
    n = len(arr)
    # First check all the values that are present in an array then go to that values as indexes
    # and increment by the size of array
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

    # Now check which value exists more than once by dividing with the size of array
    for i in range(0, n):
        if (arr[i] / n) > 1:
            print(i, end=" ")


arr = [1, 6, 3, 1, 3, 6, 6]
find_duplicate_numbers(arr)
