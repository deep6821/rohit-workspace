import sys


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# The worst case time complexity of this method is O(n2), but it works in O(n) on average.
def kth_smallest(arr, l, r, k):
    # If k is smaller than number of elements in array
    if 0 < k <= r - l + 1:

        # Partition the array around last element and get position of pivot element in sorted array
        pos = partition(arr, l, r)

        # If position is same as k
        if pos - l == k - 1:
            return arr[pos]

        if pos - l > k - 1:  # If position is more,
            # recur for left subarray
            return kth_smallest(arr, l, pos - 1, k)

        # Else recur for right subarray
        return kth_smallest(arr, pos + 1, r, k - pos + l - 1)

    # If k is more than number of elements in array
    return sys.maxsize


# Driver Code
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is", kth_smallest(arr, 0, n - 1, k))
