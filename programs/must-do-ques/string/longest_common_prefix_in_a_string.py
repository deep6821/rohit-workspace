"""
A prefix is a collection of characters at the beginning of a string. For instance, “mi” is a prefix of “mint”
and the longest common prefix between “mint”, “mini”, and “mineral” is “min”.

Different approaches:
1. Word by Word Matching
2. Character by Character Matching
3. Divide and Conquer
4. Binary Search.
5. Using Trie
6. Using Sorting
"""


def common_prefix_util(str1, str2):
    result = ""
    n1 = len(str1)
    n2 = len(str2)

    # Compare str1 and str2
    i = 0
    j = 0
    while i <= n1 - 1 and j <= n2 - 1:
        if str1[i] != str2[j]:
            break

        result += str1[i]
        i += 1
        j += 1

    return result


# Time Complexity : O(N M) -->, Since we are iterating through all the strings and for each string we are
# iterating though each characters where N = Number of strings and M = Length of the largest string string
# Auxiliary Space : To store the longest prefix string we are allocating space which is O(M).
def common_prefix_word_by_word(arr):
    n = len(arr)
    prefix = arr[0]
    for i in range(1, n):
        prefix = common_prefix_util(prefix, arr[i])
    return prefix


# Time Complexity : O(N M) --> Since we are iterating through all the characters of all the strings,
# where N = Number of strings and M = Length of the largest string string
# Auxiliary Space : To store the longest prefix string we are allocating space which is O(M).
def common_prefix_character_by_character(arr):
    min_length = len(arr[0])
    n = len(arr)
    result = ""
    for i in range(1, n):
        if len(arr[i]) < min_length:
            min_length = len(arr[i])

    for i in range(min_length):
        current = arr[0][i]
        for j in range(1, n):
            if arr[j][i] != current:
                return result
        result = result + current

    return result


# We first divide the arrays of string into two parts. Then we do the same for left part and after that for
# the right part. We will do it until and unless all the strings become of length 1.
# Now after that, we will start conquering by returning the common prefix of the left and the right strings.

# Time Complexity : Since we are iterating through all the characters of all the strings, so we can say that
# the time complexity is O(N M) where,
# Auxiliary Space : To store the longest prefix string we are allocating space which is O(M Log N).
def common_prefix_using_divide_and_conquer(arr, low, high):
    if low == high:
        return arr[low]

    if low < high:
        mid = low + (high - low) // 2
        str1 = common_prefix_using_divide_and_conquer(arr, low, mid)
        str2 = common_prefix_using_divide_and_conquer(arr, mid + 1, high)
        return common_prefix_util(str1, str2)


def common_prefix_using_binary_search(arr):
    return arr


# The idea is to sort the array of strings and find the common prefix of the first and last string of the
# sorted array.

# Time Complexity: O(MAX * n * log n ) where n is the number of strings in the array and MAX is maximum
# number of characters in any string. Please note that comparison of two strings would take at most O(MAX)
# time and for sorting n strings, we would need O(MAX * n * log n ) time.
def common_prefix_using_sorting(arr):
    size = len(arr)

    # if size is 0, return empty string
    if size == 0:
        return ""

    if size == 1:
        return arr[0]

    # sort the array of strings
    arr.sort()

    # find the minimum length from first and last string
    end = min(len(arr[0]), len(arr[size - 1]))

    # find the common prefix between the first and last string
    i = 0
    while i < end and arr[0][i] == arr[size - 1][i]:
        i += 1

    pre = arr[0][0: i]
    return pre


arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
res1 = common_prefix_word_by_word(arr)
res2 = common_prefix_character_by_character(arr)
res3 = common_prefix_using_divide_and_conquer(arr, 0, len(arr) - 1)
res4 = common_prefix_using_binary_search(arr)
# res5 = common_prefix_using_trie()
re6 = common_prefix_using_sorting(arr)
