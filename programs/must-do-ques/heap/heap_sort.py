"""
Time complexity:It takes O(logn) for heapify and O(n) for constructing a heap.
Hence, the overall time complexity of heap sort using min heap or max heap is O(nlogn)

Note :Heap Sort using min heap sorts in descending order where as max heap sorts in ascending order
"""


def min_heapify(arr, n, i):
    left = 2 * i
    right = 2 * i + 1

    # If left child is smaller than root
    if left < n and arr[left] < arr[i]:
        smallest = left
    else:
        smallest = i

    # If right child is smaller than smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

    return arr


def max_heapify(arr, n, i):
    left = 2 * i
    right = 2 * i + 1

    if left < n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

    return arr


def heap_sort1(arr):
    n = len(arr)

    # Build a max heap.
    for i in range(int(n / 2), -1, -1):
        max_heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        max_heapify(arr, i, 0)

    return arr


def heap_sort2(arr):
    n = len(arr)

    # Build a min heap.
    for i in range(int(n / 2), -1, -1):
        min_heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        min_heapify(arr, i, 0)

    return arr


arr1 = [12, 11, 13, 5, 6, 7]
arr2 = [4, 6, 3, 2, 9]
result1 = heap_sort1(arr1)
print("Max Heap Sort :")
for i in range(0, len(result1)):
    print(result1[i], end=" ")

print("\nMin Heap Sort: ")
result2 = heap_sort2(arr2)
for i in range(len(result2)):
    print(result2[i], end=" ")
