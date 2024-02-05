"""
Maximum distance between two occurrences of same element in array
Given an array with repeated elements, the task is to find the maximum distance two occurrences of an
element.

- A simple solution for this problem is to one by one pick each element from array and find its first and
last occurrence in array and take difference of first and last occurrence for maximum distance.
Time complexity for this approach is O(n2).

- An efficient solution for this problem is to use hashing. The idea is to traverse input array and store
index of first occurrence in a hash map. For every other occurrence, find the difference between index
and the first index stored in hash map. If difference is more than result so far, then update the result.
"""


# Time complexity : O(n) under the assumption that unordered_map’s search and insert operations take O(1)
# time.
def max_distance(arr):
    n = len(arr)
    # Used to store element to first index mapping
    temp_dict = {}
    # Traverse elements and find maximum distance between same occurrences with the help of map.
    max_dist = 0
    for i in range(n):
        # If this is first occurrence of element, insert its index in map
        if arr[i] not in temp_dict.keys():
            temp_dict[arr[i]] = i

        # Else update max distance
        else:
            max_dist = max(max_dist, i - temp_dict[arr[i]])

    return max_dist


def count_consecutive_occurrences1(s):
    count = 1
    freq = {}
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            freq[s[i]] = count
        else:
            count = 1
    print(freq)


def count_consecutive_occurrences2(s):
    count = 1
    freq = {}
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            freq[s[i]] = count
        else:
            freq[s[i]] = count
            count = 1
    print(freq)


def count_frequency_of_word1(words):
    # from collections import Counter
    # counts = Counter(words)
    # print(counts)
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)


def check_if_one_tuple_is_subset_of_other():
    test_tup1 = (10, 4, 5, 6)
    test_tup2 = (5, 10)
    res1 = set(test_tup2).issubset(test_tup1)
    print(res1)
    res2 = all(ele in test_tup1 for ele in test_tup2)
    print(res2)


# Driver Program
if __name__ == '__main__':
    print(max_distance([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))
    count_consecutive_occurrences1("100011010")
    count_consecutive_occurrences2("GeeeEEKKKss")
    count_frequency_of_word1("100011010")
