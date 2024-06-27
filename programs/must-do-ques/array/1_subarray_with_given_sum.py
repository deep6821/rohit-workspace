"""
Given an unsorted array of non-negative integers, find a continuous subarray which adds to a
given number.

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices: 20 + 3 + 10 = 33
"""

"""
1. Initialize an empty result list and get the length of the array.
2. Iterate through the array with two nested loops.
3. The outer loop sets the starting point of the subarray.
4. The inner loop calculates the sum of the subarray starting from the outer loop index.
5. If the sum matches the target, it prints the starting and ending indices and stores the result.
6. If the sum exceeds the target or if the end of the array is reached, it breaks the inner loop.

The time complexity is O(n^2) due to the nested loops and and SC: 0(1)
"""


def subarray_sum(arr, s):
    result = []
    n = len(arr)
    for i in range(0, n):
        curr_sum = arr[i]
        j = i + 1
        while j <= n:
            if curr_sum == s:
                print("Sum found between {} and {}".format(i, j - 1))
                result.append((i, j - 1))
                # return 1

            if curr_sum > s or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print(result)
    print("No subarray found")
    return 0


"""
This function uses a sliding window (or two-pointer) technique to find the continuous subarray 
that adds up to a given sum s. 

Here's the step-by-step explanation:

1. Initialization:
  n: Length of the array.
  curr: The current sum, starting with the first element (arr[0]).
  i: The end pointer, starting from the second element (1).
  start: The start pointer, starting from the first element (0).

2. Iterate through the array:
  The while loop runs until i is less than or equal to n (the length of the array).
  
3. Adjust the window:
  Inner while loop: If the current sum (curr) is greater than the target sum (s), reduce the 
  sum by removing elements from the start of the current window. This is done by subtracting 
  arr[start] from curr and incrementing the start pointer.
  
  This step ensures that we only keep the sum of elements between the current start and i-1 
  within the window.

4. Check for the target sum:
If curr equals s, print the indices start to i-1 and return 1.

5. Expand the window:
  If the end pointer (i) is still within bounds (i < n), add the next element (arr[i]) to the 
  current sum (curr).

  Increment the end pointer (i).

6. If no subarray is found:
  If the loop completes without finding the target sum, print "No subarray with given sum 
  exists".
  
# TC: 0(n) and SC: 0(1)
"""


def subarray_sum2(arr, s):
    n = len(arr)
    curr = arr[0]
    i = 1
    start = 0
    while i <= n:
        while curr > s and start < i - 1:
            curr = curr - arr[start]
            start += 1

        if curr == s:
            print("Sum found between {} and {}".format(start, i - 1))
            return 1

        if i < n:
            curr = curr + arr[i]

        i += 1

    print("No subarray with given sum exists")


"""
This function uses a hash map (dictionary) to handle cases where the array may include negative
numbers. 

Here's the step-by-step explanation:
1. Initialization:
  n: Length of the array.
  dict: A dictionary to store the cumulative sum and its index.
  curr: The current cumulative sum, initialized to 0.

2. Iterate through the array:
For each element in the array, update the cumulative sum (curr) by adding the current element 
(arr[i]).

3. Check for the target sum:
If the cumulative sum (curr) equals the target sum (s), print the indices 0 to i and return.

4. Check for the required subarray:
If the difference between the current cumulative sum (curr) and the target sum (s) exists in 
the dictionary, it means there is a subarray that sums to s. Print the indices from the next 
element after the stored index to the current index and return.

5. Update the dictionary:
Store the current cumulative sum (curr) with its index (i) in the dictionary.

6. If no subarray is found:
If the loop completes without finding the target sum, print "No subarray with given sum exists".

# Time complexity: O(n).
# Auxiliary space: O(n)
"""


def subarray_sum_for_negative_no(arr, s):
    n = len(arr)
    dict = {}
    curr = 0
    for i in range(0, n):
        curr = curr + arr[i]

        if curr == s:
            print("Sum found between indexes 0 to", i)
            return

        if (curr - s) in dict:
            print("Sum found between indexes", dict[curr - s] + 1, "to", i)
            return
        dict[curr] = i

    print("No subarray with given sum exists")


arr = [1, 2, 3, 4, 5]
subarray_sum([4, 8, 1, 3, 9, 5, 11], 10)
subarray_sum(arr, s=5)
subarray_sum2(arr, s=33)
subarray_sum_for_negative_no([10, 2, -2, -20, 10], s=-10)
