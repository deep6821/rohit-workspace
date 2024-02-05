"""
This algorithm works by repeatedly finding the minimum element in the list and
placing it at the beginning. This way, the algorithm maintains two lists:

1. the sublist of already-sorted elements, which is filled from left to right
2. the sublist of the remaining unsorted elements that need to be sorted

In other words, this algorithm works by iterating over the list and swapping
each element with the minimum (or maximum) element found in the unsorted list
with that in the sorted list.

Time complexity:
----------------
The time complexity of this code is in O(n^2), because finding a minimum number
in the list requires iterating over the entire list for each element of the
given list.

The quadratic time complexity makes it impractical for large inputs.
"""


def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Driver code to test above
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)
    # Printing Sorted lst
    print("Sorted lst: ", lst)
