"""
Merge sort is a recursive divide & conquer algorithm that essentially divides
a given list into two halves, sorts those halves, and merges them in order.

The base case is to merge two lists of size 1 so, eventually, single elements
are merged in order; the merge part is where most of the heavy lifting happens.


Time complexity:
----------------
The time complexity of merge sort is nlog(n).
"""


def merge_sort(lst):
    """
    Merge sort function
    :param lst: lst of unsorted integers
    """
    if len(lst) > 1:
        mid = len(lst) // 2  # Mid of the list
        left = lst[:mid]  # Dividing the list elements into 2 halves
        right = lst[mid:]

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        # Initializing index variables
        i = 0
        j = 0
        k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


# Driver code to test the above code
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)
    print("Sorted list is: ", lst)
