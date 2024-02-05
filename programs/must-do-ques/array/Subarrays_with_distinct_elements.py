# Python program to print all distinct elements in a given array
# The elements are printed in same order as they are in input array.
# Average Time Complexity: O(n)


def print_distinct(arr, n):
    # Creates an empty hash set
    s = dict()

    # Traverse the input array
    for i in range(n):

        # If not present, then put it in hashtable and print it
        if arr[i] not in s.keys():
            s[arr[i]] = arr[i]
            print(arr[i], end=" ")


arr = [10, 5, 3, 4, 3, 5, 6]
n = 7
print_distinct(arr, n)

"""
Subarrays with distinct elements:
---------------------------------
Given an array, the task is to calculate the sum of lengths of contiguous sub arrays having all
elements distinct.

Input : [1, 2, 3]
Output:
    [1, 2, 3] -> 3
    [1], [2], [3] -> 3
    [1, 2], [2, 3] -> 4

    Sum of lengths = 3 + 3 + 4 = 10
    
Approach:
An efficient solution is based on the fact that if we know all elements in a subarray arr[i..j] are 
distinct, sum of all lengths of distinct element subarrays in this sub array is ((j-i+1)*(j-i+2))/2. 
How? the possible lengths of subarrays are 1, 2, 3,……, j – i +1. So, 
the sum will be ((j – i +1)*(j – i +2))/2.


We first find largest subarray (with distinct elements) starting from first element. We count sum of 
lengths in this subarray using above formula. For finding next subarray of the distinct element, we 
increment starting point, i and ending point, j unless (i+1, j) are distinct. If not possible, then 
we increment i again and move forward the same way.
"""


# Returns sum of lengths contiguous of all subarrays with distinct elements.
# Time Complexity: O(n)
def sum_of_length(arr, n):
    # For maintaining distinct elements.
    s = []

    # Initialize ending point and result
    j = 0
    ans = 0

    # Fix starting point
    for i in range(n):
        # Find ending point for current subarray with distinct elements.
        while j < n and (arr[j] not in s):
            s.append(arr[j])
            j += 1

        # Calculating and adding all possible length subarrays in arr[i..j]
        ans += ((j - i) * (j - i + 1)) // 2

        # Remove arr[i] as we pick new stating point from next
        s.remove(arr[i])

    return ans


# Driven Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    print(sum_of_length(arr, n))

"""
Count of subarrays having exactly K distinct elements:
-----------------------------------------------------
nput: arr[] = {2, 1, 2, 1, 6}, K = 2
Output: 7
{2, 1}, {1, 2}, {2, 1}, {1, 6}, {2, 1, 2},
{1, 2, 1} and {2, 1, 2, 1} are the only valid subarrays.

Approach: 
To directly count the subarrays with exactly K different integers is hard but to find the count of 
subarrays with at most K different integers is easy. So the idea is to find the count of subarrays 
with at most K different integers, let it be C(K), and the count of subarrays with at most (K – 1) 
different integers, let it be C(K – 1) and finally take their difference, C(K) – C(K – 1) which is 
the required answer.

Count of subarrays with at most K different elements can be easily calculated through the sliding 
window technique. The idea is to keep expanding the right boundary of the window till the count of 
distinct elements in the window is less than or equal to K and when the count of distinct elements 
inside the window becomes more than K, start shrinking the window from the left till the count 
becomes less than or equal to K. Also for every expansion, keep counting the subarrays as right – 
left + 1 where right and left are the boundaries of the current window.
"""


# Function to return the count of subarrays
# with at most K distinct elements using the sliding window technique
# Time Complexity: O(N)
# Space Complexity: O(N)
def atMostK(arr, n, k):
    # To store the result
    count = 0

    # Left boundary of window
    left = 0

    # Right boundary of window
    right = 0

    # Map to keep track of number of distinct
    # elements in the current window
    map = {}

    # Loop to calculate the count
    while right < n:

        if arr[right] not in map:
            map[arr[right]] = 0

        # Calculating the frequency of each
        # element in the current window
        map[arr[right]] += 1

        # Shrinking the window from left if the
        # count of distinct elements exceeds K
        while len(map) > k:

            if arr[left] not in map:
                map[arr[left]] = 0

            map[arr[left]] -= 1

            if map[arr[left]] == 0:
                del map[arr[left]]

            left += 1

        # Adding the count of subarrays with at most
        # K distinct elements in the current window
        count += right - left + 1
        right += 1

    return count


# Function to return the count of subarrays with exactly K distinct elements
def exactlyK(arr, n, k):
    # Count of subarrays with exactly k distinct elements is equal to the difference of the
    # count of subarrays with at most K distinct elements and the count of subararys with
    # at most (K - 1) distinct elements
    return (atMostK(arr, n, k) -
            atMostK(arr, n, k - 1))


# Driver code
if __name__ == "__main__":
    arr = [2, 1, 2, 1, 6]
    n = len(arr)
    k = 2
    print(exactlyK(arr, n, k))
