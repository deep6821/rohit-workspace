"""
Trapping Rain Water:
--------------------
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it is able to trap after raining.

Input: arr[]   = {2, 0, 2}
Output: 2
Explanation: We can trap 2 units of water in the middle gap.

Basic Insight:
An element of the array can store water if there are higher bars on left and right. The amount of water to be
stored in every element can be found out by finding the heights of bars on the left and right sides. The idea
is to compute the amount of water that can be stored in every element of the array.
"""


# Time Complexity: O(n2).
# Space Complexity: O(1).
def rainwater_tapping(arr):
    """
    Algorithm:
    1. Traverse the array from start to end.
    2. For every element, traverse the array from start to that index and find the maximum height (a) and traverse
    the array from the current index to end and find the maximum height (b).
    3. The amount of water that will be stored in this column is min(a,b) – array[i], add this value to total
    amount of water stored
    4. Print the total amount of water stored.
    """
    n = len(arr)
    res = 0
    for i in range(1, n - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

        res = res + min(left, right) - arr[i]

    print(res)


# Time Complexity: O(n).
# Space Complexity: O(n).
def rainwater_tapping2(arr):
    """
    Algorithm:
    1. Create two array left and right of size n. create a variable max_ = INT_MIN.
    2. Run one loop from start to end. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign
    left[i] = max_
    3. Update max_ = INT_MIN.
    4. Run another loop from end to start. In each iteration update max_ as max_ = max(max_, arr[i]) and also
    assign right[i] = max_
    5. Traverse the array from start to end.
    6. The amount of water that will be stored in this column is min(a,b) – array[i],(where a = left[i] and
    b = right[i]) add this value to total amount of water stored
    7. Print the total amount of water stored.
    """
    n = len(arr)
    left = [0] * n
    right = [0] * n
    water = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        right[j] = max(right[j + 1], arr[j])

    for i in range(0, n):
        water = water + min(left[i], right[i] - arr[i])

    return water


# Time Complexity: O(n).
# Auxiliary Space: O(1).
def rainwater_tapping3(arr, n):
    """
    Algorithm:
    1. Loop from index 0 to the end of the given array.
    2. If a wall greater than or equal to the previous wall is encountered then make note of the index of that
    wall in a var called prev_index.
    3. Keep adding previous wall’s height minus the current (ith) wall to the variable water.
    4. Have a temporary variable that stores the same value as water.
    5. If no wall greater than or equal to the previous wall is found then quit.
    6. If prev_index < size of the input array then subtract the temp variable from water, and loop from end of
    the input array to prev_index and find a wall greater than or equal to the previous wall (in this case, the
    last wall from backwards).
    """
    size = n - 1
    # Let the first element be stored as previous, we shall loop from index 1
    prev = arr[0]

    # To store previous wall's index
    prev_index = 0
    water = 0
    # To store the water until a larger wall is found, if there are no larger walls  then delete temp value from water
    temp = 0
    for i in range(1, size + 1):
        # If the current wall is taller than the previous wall then make current
        # wall as the previous wall and its index as previous wall's index  for the subsequent loops
        if arr[i] >= prev:
            prev = arr[i]
            prev_index = i

            # Because larger or same height wall is found
            temp = 0
        else:
            # Since current wall is shorter than the previous, we subtract previous wall's height from the current
            # wall's height and add it to the water
            water += prev - arr[i]

            # Store the same value in temp as well If we dont find any larger wall then
            # we will subtract temp from water
            temp += prev - arr[i]

        # If the last wall was larger than or equal to the previous wall then prev_index would be equal to size of
        # the array (last element) If we didn't find a wall greater than or equal
        # to the previous wall from the left then prev_index must be less than the index of the last element
        if prev_index < size:
            # Temp would've stored the water collected from previous largest wall till the end of array if no larger
            # wall was found then it has excess water and remove that from 'water' var
            water -= temp

            # We start from the end of the array, so previous should be assigned to the last element
            prev = arr[size]

            # Loop from the end of array up to the 'previous index' which would contain the "largest wall from the
            # left"
            for i in range(size, prev_index - 1, -1):

                # Right end wall will be definitely smaller than the 'previous index' wall
                if arr[i] >= prev:
                    prev = arr[i]
                else:
                    water += prev - arr[i]

        # Return the maximum water
        return water


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
rainwater_tapping(arr)
print(rainwater_tapping3(arr, len(arr)))
