# Time Complexity: The worst case time complexity of code/algorithm is O(m*n).
# Auxiliary Space : O(1)
def merge_two_sorted_array1(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    for i in range(n2 - 1, -1, -1):
        last = arr1[n1 - 1]
        j = n1 - 2
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1

        if j != n1 - 2 or last > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = last

    print(arr1, arr2)


# Time Complexity : O(n1 + n2)
# Auxiliary Space : O(n1 + n2)
def merge_two_sorted_array2(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    result = [None] * (n1 + n2)

    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
            k += 1
        else:
            result[k] = arr2[j]
            j += 1
            k += 1

    while i < n1:
        result[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        result[k] = arr2[j]
        j += 1
        k += 1

    print(result)


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge_two_sorted_array1(arr1, arr2)
merge_two_sorted_array2(arr1, arr2)
