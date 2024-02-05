"""
Median in a stream of integers (running integers)
-------------------------------------------------

Given that integers are read from a data stream. Find median of elements read so for in efficient way. For simplicity
assume there are no duplicates.

For example, let us consider the stream 5, 15, 1, 3 …
-----------------------------------------------------
After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

***********************************************************************************************************************
- When the input size is odd, we take the middle element of sorted data.
- If the input size is even, we pick average of middle two elements in sorted stream.
***********************************************************************************************************************
"""

import heapq

if 0:
    from heapq import heappop, heappush, heappushpop

    N = int(input())
    S = [int(input()) for i in range(N)]
    L, R = [], [S[0]]

    for i in range(N):
        print("%.1f" % R[0] if len(R) > len(L) else (R[0] - L[0]) / 2.0)
        if i == N - 1:
            break
        heappush(L, -heappushpop(R, S[i + 1]))
        if len(L) > len(R):
            heappush(R, -heappop(L))

if 1:
    # O(N log N),
    def left_child(k):
        return 2 * k + 1


    def right_child(k):
        return 2 * k + 2


    def parent(k):
        return (k - (2 if k % 2 == 0 else 1)) // 2


    def swap(heap, j, k):
        heap[j], heap[k] = heap[k], heap[j]


    def push(heap, val):
        heap.append(val)
        siftdown(heap)


    def pop(heap):
        k = len(heap) - 1
        swap(heap, 0, k)
        result = heap.pop()
        siftup(heap)
        return result


    def peek(heap):
        return heap[0]


    def siftdown(heap):
        child = len(heap) - 1
        p = parent(child)
        while child > 0:
            if heap[p] > heap[child]:
                swap(heap, p, child)
                child, p = p, parent(p)
            else:
                break


    def siftup(heap):
        size = len(heap)
        p = 0
        l, r = left_child(p), right_child(p)
        while r < size:
            c = l if heap[l] < heap[r] else r
            if heap[c] < heap[p]:
                swap(heap, c, p)
                p = c
                l, r = left_child(p), right_child(p)
            else:
                break
        if l < size and heap[l] < heap[p]:
            swap(heap, l, p)


    max_heap, min_heap = [], []
    max_heap_size = min_heap_size = 0
    median = 0

    n = int(input())
    for _ in range(n):
        val = int(input())

        # Insert
        if val > median:
            push(min_heap, val)
            min_heap_size += 1
        else:
            push(max_heap, -val)
            max_heap_size += 1

        # Restore balance
        if min_heap_size > max_heap_size + 1:
            push(max_heap, -pop(min_heap))
            max_heap_size += 1
            min_heap_size -= 1
        elif max_heap_size > min_heap_size + 1:
            push(min_heap, -pop(max_heap))
            min_heap_size += 1
            max_heap_size -= 1

        # Update median
        if min_heap_size < max_heap_size:
            median = - float(peek(max_heap))
        elif max_heap_size < min_heap_size:
            median = float(peek(min_heap))
        else:
            median = (peek(min_heap) - peek(max_heap)) / 2.0

        print(median)
