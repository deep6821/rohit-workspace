"""
Consider a sorted list, of n integers. We are required to find if a particular
integer value exists in the given list or not.

Time complexity:
----------------
If we start at the middle of the list, it’s either we are lucky and the element
matches or we discard half of the list. In the worst case, we will repeatedly
discard half of the sub-lists from the previous step until the list can no
longer be subdivided, i.e., it is of size 1.

An array of size n can be divided into halves logn times until we reach a
sublist of size 1.

Hence, the time complexity of this solution of finding an element in a sorted
list is O(logn).
"""


# Time Complexity: T(n) = T(n/2) + c --> 0(logn)
# Space Complexity: O(Logn) recursion call stack space.
def binary_search(arr, left, right, key):
    """

    :param arr:
    :param left:
    :param right:
    :param key:
    :return: The index of the key in the list if found, -1 otherwise
    """
    if left <= right:
        mid_element = (left + right) // 2

        # If the required element is found at the middle index
        if arr[mid_element] == key:
            return mid_element

        # If the required element is smaller than the element at the middle
        # index. It can only be present in the left sub-list
        if arr[mid_element] > key:
            return binary_search(arr, left, mid_element - 1, key)

        # Otherwise, it would be present in the right sub-list
        return binary_search(arr, mid_element + 1, right, key)

    # If the element is not in the list
    return -1


# Time Complexity: T(n) = T(n/2) + c --> 0(logn)
# Space Complexity: O(1)
def iterative_binary_search(arr, left, right, key):
    while left <= right:
        mid_element = (left + right) // 2
        if arr[mid_element] == key:
            return mid_element
        elif arr[mid_element] > key:
            right = mid_element - 1
        else:
            left = mid_element + 1
    return -1


if __name__ == "__main__":
    lst = [2, 4, 7, 25, 60]
    key = 25
    result = binary_search(lst, 0, len(lst) - 1, key)
    print("result: ", result)
    result1 = iterative_binary_search(lst, 0, len(lst) - 1, key)
    print("result1: ", result1)
