"""
Implement a function that sorts a list of 0s, 1s and 2s. This is called
the Dutch National Problem. Since the number O can be represented by the blue
color, 1 by the white color, and 2 as the red color, the task is to transform
the list input to the Dutch flag.

Input:
------
An array of 0s, 1s, and 2s

Output:
-------
An array where the numbers 0, 1, and 2 are sorted

Sample input:
-------------
lst = [2, 0, 0, 1, 2, 1, 0]

Sample output:
result = [0, 0, 0, 1, 1, 2, 2]

Solution:
---------
The algorithm keeps track of the index of last zero in the list (i), the
position of the last two present (j), and an index mid that moves ahead only
when it has found a 1 or when a 0 is swapped with any 1.

Time complexity:
---------------
Since we are arranging the elements of the list in a single iteration, the
complexity is O(n).
"""


def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    size = len(lst)
    i = 0
    mid = 0
    j = size - 1

    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1

    return lst


# Driver to test above code
if __name__ == '__main__':
    lst = [2, 0, 0, 1, 2, 1]

    print(dutch_national_flag(lst))
