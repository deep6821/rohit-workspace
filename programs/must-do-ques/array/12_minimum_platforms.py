"""
Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number
of platforms required for the railway station so that no train waits.

We are given two arrays which represent arrival and departure times of trains that stop.
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explantion: There are at-most three trains at a time (time between 11:00 to 11:20)

Algorithm:
1. Sort the arrival and departure time of trains.
2. Create two pointers i=0, and j=0 and a variable to store ans and current count plat
3. Run a loop while i<n and j<n and compare the ith element of arrival array and jth element of departure array.
4. if the arrival time is less than or equal to departure then one more platform is needed so increase the
count, i.e. plat++ and increment i
5. Else if the arrival time greater than departure then one less platform is needed so decrease the count,
i.e. plat++ and increment j
6. Update the ans, i.e ans = max(ans, plat).
"""


# Time Complexity:  O(n log n)
# Space Complexity: O(1).
def find_platform(arr, dep, n):
    # Sort arrival and departure arrays
    arr.sort()
    dep.sort()

    # plat_needed indicates number of platforms needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in merge sort to process  all events in sorted order
    while i < n and j < n:

        # If next event in sorted order is arrival, increment count of platforms needed
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1

        # Else decrement count of platforms needed
        elif arr[i] > dep[j]:
            plat_needed -= 1
            j += 1

        # Update result if needed
        if plat_needed > result:
            result = plat_needed

    return result


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",find_platform(arr, dep, n))