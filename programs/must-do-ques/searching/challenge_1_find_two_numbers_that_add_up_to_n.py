"""
In this problem, you have to implement the find_sum(lst, n) function which will
take a list lst and number n as inputs and return two numbers from the list
that add up to n.

Sample input:
-------------
lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81

Sample output:
--------------
result = [21, 60]
"""


# Solution #1: brute force
# Time complexity: since we iterate over the entire list of nn elements,
# the time complexity is O(n^2)
def find_sum1(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n and i != j:
                return [lst[i], lst[j]]


# Solution #2: sorting the list
# Time complexity: since most popular sorting functions take O(nlogn)

# Explanation: let’s assume the built-in function in Python,.sort() function
# takes the same. Then, a binary search for each element takes O(logn), so a
# binary search for all n elements will take O(nlogn). So, the overall time
# complexity is O(nlogn).
def binary_search(lst, item):
    """
    Binary Search helper function
    :param lst: A list of integers
    :param item: An item to be searched in the list
    """

    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if lst[mid] == item:
            found = mid
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    lst.sort()

    for j in lst:
        index = binary_search(lst, n - j)
        if index:
            return [j, n - j]


# Solution #3: using a dictionary
# Time complexity: each lookup is a constant time operation. Overall, the run
# time of this approach is O(n)

# Explanation: the best way to solve this problem is to insert every element
# into a dictionary (or hash table, but we’ll study this later). This takes
# O(n) as the constant time insertion. We are checking the dictionary first and
# if the difference (sum-element) is not found, then, we insert the element in
# the dictionary. So, for every element in the list, we can just look up its
# complement, T-xT−x, and if found, return T-x and x. Here, T is the
# sum-element and x is an element in the list. If the difference of T and x is
# available in the dictionary, then, it means the two elements have been found.
def using_dictionary(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = {}
    for ele in lst:
        try:
            found_values[n - ele]
            return [n - ele, ele]
        except:
            found_values[ele] = 0

    return False


# Solution #4: Using the python set()
# Time complexity: the time complexity of the solution above is in O(n)
def using_set(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = set()

    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)

    return False


# Driver code to test above
if __name__ == '__main__':
    print(find_sum1([1, 2, 3, 4], 5))
