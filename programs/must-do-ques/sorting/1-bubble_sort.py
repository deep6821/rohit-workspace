"""
This is another famous sorting algorithm also known as ‘sinking sort’. It works
by comparing adjacent pairs of elements and swapping them if they are in the
wrong order. This is repeated until the list is sorted.

Think of it this way: a bubble passes over the list, ‘catches’ the
maximum/minimum element, and brings it over to the right side.

The time complexity of this code is O(n^2).
"""


def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# Driver code to test above
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)
    print("Sorted list is: ", lst)
