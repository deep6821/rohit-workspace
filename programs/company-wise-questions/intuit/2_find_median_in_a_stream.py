"""
Median:
------
1. When the input size is "odd": we take the middle element of sorted data
2. If the input size is "even": we pick average of middle two elements in sorted stream.

Ex:
After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4
"""

from heapq import *


# Time Complexity: O(n Log n) -> to insert element in min heap is log n. So to insert n element is O( n log n).
# Auxiliary Space : O(n) -> to store the elements in Heap is O(n).
class FindMedian:
    """
    We have a max amd min heaps. The tops of these heaps represent the middle
    of the stream so far.
    """

    def __init__(self):
        # max heap representing the sorted left half of the stream
        self.min_heap = []
        # min heap representing the sorted right half of the stream
        self.max_heap = []

    # Time Complexity: O(log n) and Space Complexity: O(n)
    def add_number(self, num: int) -> None:
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    # Time Complexity: O(1) and Space Complexity: O(1)
    def find_median(self) -> float:
        has_even_count = len(self.max_heap) == len(self.min_heap)
        if has_even_count:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(self.min_heap[0])


if __name__ == "__main__":
    obj = FindMedian()
    for _ in range(3):
        obj.add_number(int(input()))
    print(obj.find_median())
