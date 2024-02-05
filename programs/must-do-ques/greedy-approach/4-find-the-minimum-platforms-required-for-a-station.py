"""
Implement a function that returns the minimum number of platforms that are
required for the train so that none of them waits.

Input #
Two lists which represent arrival and departure times of trains that stop

Output #
Minimum number of platforms required

Sample input #
arrival= [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

Sample output #
result = 3

Solution 1: brute force: O(n2)

Solution 2: sorting: O(nlogn)
Explanation:
-----------
The idea is to consider all events in sorted order. Once we have all events in
sorted order, we can trace the number of trains at any given time and check for
the trains that have arrived, but have not departed. That way, we know how many
platforms we need at that time and can take the maximum of all such instances

"""


def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of Arrival Timing
    :param departure: A list of Departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    # Sort arrival and departure lists
    n = len(arrival)  # Length of the arrival list
    arrival.sort()
    departure.sort()

    # plat_needed indicates number of platforms needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in merge sort to process all events in sorted order
    while i < n and j < n:

        # If next event in sorted order is arrival, increment count of platforms needed
        if arrival[i] < departure[j]:

            plat_needed += 1
            i += 1

            # Update result if needed
            if plat_needed > result:
                result = plat_needed

        # Else decrement count of platforms needed
        else:
            plat_needed -= 1
            j += 1

    return result


# Driver code to test above function
if __name__ == '__main__':
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))
