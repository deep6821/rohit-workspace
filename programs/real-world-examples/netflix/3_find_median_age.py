"""
Time Complexity:
----------------
The time complexity of the Insert Age will be O(logn) because we inserted in the heap.
The time complexity of the Find Median will be O(1) because we can find the median from the top elements of the heaps.

Memory complexity:
------------------
The memory complexity will be O(n) because we will be storing all the numbers at any time.
"""

from heapq import *


class MedianOfAges:
    maxHeap = []
    minHeap = []

    def insert_age(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0


# Driver code
medianAge = MedianOfAges()
medianAge.insert_age(22)
medianAge.insert_age(35)
print("The recommended content will be for ages under: " + str(medianAge.find_median()))
medianAge.insert_age(30)
print("The recommended content will be for ages under: " + str(medianAge.find_median()))
medianAge.insert_age(25)
print("The recommended content will be for ages under: " + str(medianAge.find_median()))
