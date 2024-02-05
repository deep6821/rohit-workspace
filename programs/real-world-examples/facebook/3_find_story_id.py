"""
Let n be the size of the list.

Time complexity:
----------------
The time complexity will be O(logn) because we are dividing the array by 2 at each step.

Space complexity:
-----------------
The space complexity will be O(1) because a constant amount of space was utilized.
"""


def find_story_id(arr, key):
    start = 0
    end = len(arr) - 1

    if start > end:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
            end = mid - 1

        elif (arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]):
            start = mid + 1

        elif arr[start] <= arr[mid] and arr[mid] <= arr[end] and key > arr[end]:
            start = mid + 1

        elif arr[end] <= arr[mid]:
            start = mid + 1

        elif arr[start] >= arr[mid]:
            end = mid - 1

        else:
            return -1

    return -1


v1 = [6, 7, 1, 2, 3, 4, 5]
print("Story(3) found at index: " + str(find_story_id(v1, 3)))
print("Story(6) found at index: " + str(find_story_id(v1, 6)))

v2 = [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]

print("Story(3) found at index: " + str(find_story_id(v2, 3)))
print("Story(6) found at index: " + str(find_story_id(v2, 6)))