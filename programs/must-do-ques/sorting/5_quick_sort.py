"""
Quick sort is the fastest-known, comparison-based sorting algorithm for lists
in the average case.

Caveat: Merge sort works better on linked lists and there are other
non-comparison-based algorithms that outperform Quick Sort

Steps for quick sort algorithm:
-------------------------------

1. Start with a list of n elements
2. Choose a pivot element from the list to be sorted
3. Partition the list into 2 unsorted sublists, such that all elements in one
   sublist are less than the pivot and all the elements in the other sublist
   are greater than the pivot
4. Elements that are equal to the pivot can go in either sublist
5. Sort each sublist recursively to yield two sorted sublists
6. Concatenate the two sorted sublists and the pivot to yield one sorted list

How to pick the pivot:
----------------------
There are two methods by which you can choose a pivot

Choose randomly:
The pivot can be picked randomly from the given elements. The chances of the
first element being picked at every recursive call with this strategy is,

Median of three strategy:
-------------------------
Pick three random elements from the list and choose their median. This strategy
ensures that the first element is not picked.

Analysis of quick sort:
-----------------------
The worst-case time complexity of quick sort is in O(n^2) although, the
occurrence is rare. This can happen when:

1. The array is already sorted in the same order
2. The array is already sorted in reverse order
3. All the elements in the array are the same

The average case complexity of quick sort is in O(nlog(n)), because for each
log(n) recursive call, the given list is iterated over.
"""
import random


def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(lst, left, right):
    """
    Partition the list on the basis of pivot
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Index of pivot
    pivot_index = choose_pivot(left, right)

    # put the pivot at the end
    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]

    # Pivot
    pivot = lst[right]
    # All the elements less than or equal to the
    i = left - 1
    # pivot go before or at i

    for j in range(left, right):
        if lst[j] <= pivot:
            # increment the index
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    # Putting the pivot back in place
    lst[i + 1], lst[right] = lst[right], lst[i + 1]
    return i + 1


def quick_sort(lst, left, right):
    """
    Quick sort function
    :param lst: lst of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    if left < right:
        # pi is where the pivot is at
        pi = partition(lst, left, right)

        # Separately sort elements before and after partition
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)


# Driver code to test above
if __name__ == '__main__':
    lst = [5, 4, 2, 1, 3]
    quick_sort(lst, 0, len(lst) - 1)
    # Printing Sorted list
    print("Sorted list: ", lst)
