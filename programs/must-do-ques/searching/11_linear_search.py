"""
1. Brute force: linear search
-----------------------------

How linear search works?
========================
Go through each element one by one. When the element you are searching for is
found, return its index.

Performance of linear search:
=============================
Linear search runs in O(n) in the worst case. This is because it makes at most
n comparisons, where n is the length of the list.
"""


def linear_search(lst, key):
    """
    Linear search function
    :param lst: lst of unsorted integers
    :param key: A key to be searched in the list
    """
    if len(lst) <= 0:  # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1  # Return -1 otherwise


# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
    key = 95

    index = linear_search(lst, key)
    if index != -1:
        print("Key:", key, "is found at index:", index)
    else:
        print(key, " is not found in the list.")
