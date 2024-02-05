"""
Input: [1, 2, 1]
Subarray: A subarray is a contiguous sequence of elements within an array.
   Ex: [1], [2], [1, 2], [2, 1], [1, 2, 1], []
   Property:
   1. A subarray should be a contiguous subsequence of the parent array.
      Ex: Invalid: [1, 1] -> Since [2] in the middle is skipped, so it is not a contiguous sequence anymore
   2. The full array itself is a subarray of itself.
   3. An empty array is a subarray of any array.
   4. You can not have duplicates in subarray. The element [1] appears twice in the array [1, 2, 1]
      but can only count [1] once as the subarray of [1, 2, 1]
   5. Order of the elements in the subarray should be the same as in the array. As a result [2, 1, 1]
      is not a subarray of [1, 2, 1]

Substring: A substring is exactly the same as a subarray.
   Input: "ara"
   Ex: "a", "r", "ar", "ra", "ara", ""

Subsequence: A subsequence is a sequence that can be derived from another sequence by deleting some
   or no elements without changing the order of the remaining elements. This means a subsequence is
   a subarray, where the rule of contiguity does not apply.

   Ex: <A, B, A>   ---> <A>, <B>, <A, B>, <B, A>, <A, A> <A, B, A>, <>


"""


def longest_sub_sequence(arr):
    print("Input array: ", arr)
    n = len(arr)
    arr.sort()
    print("Sorted array: ", arr)
    result, count = 0, 0
    temp = [arr[0]]
    for i in range(1, n):
        print("\n -----------")
        if arr[i] != arr[i - 1]:
            temp.append(arr[i])
            print("TT: ", temp)

    print("temp: ", temp)
    for i in range(len(temp)):
        if i > 0 and temp[i] == temp[i - 1] + 1:
            count += 1
        else:
            count = 1
        result = max(result, count)

    return result


print(longest_sub_sequence([1, 9, 3, 10, 4, 20, 2]))
